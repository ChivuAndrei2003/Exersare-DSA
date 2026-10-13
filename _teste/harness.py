"""Ruleaza solutia utilizatorului pe teste, in Pyodide (browser) sau CPython (tools/build_tests.py).

Fiecare problema are un `spec` (vezi tools/specs.py) care spune cum se construiesc argumentele
(liste inlantuite, arbori, grafuri, clase de design) si cum se compara rezultatul.
"""
import collections
import copy
import hashlib
import io
import json
import linecache
import math
import random
import sys
import time
import traceback

sys.setrecursionlimit(20000)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val})'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val})'


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f'Node({self.val})'


PRELUDE = '''
from typing import *
import collections, heapq, bisect, math, itertools, functools, string, re, random, operator, sys
from collections import *
from heapq import *
from bisect import *
from itertools import *
from functools import *
from math import inf, gcd, sqrt, ceil, floor, log, log2, comb, isqrt, factorial
'''


class Rejected(Exception):
    """Rezultat care nu poate fi evaluat (ex. lista cu ciclu returnata)."""


# ---------- conversii ----------
def build_list(a):
    dummy = cur = ListNode()
    for v in a:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def dump_list(head, limit=200000):
    out = []
    while head is not None:
        if not isinstance(head, ListNode):
            raise Rejected(f'Lista contine un obiect care nu e ListNode: {head!r}')
        out.append(head.val)
        if len(out) > limit:
            raise Rejected('Lista returnata are un ciclu (sau e prea lunga).')
        head = head.next
    return out


def build_tree(a):
    if not a or a[0] is None:
        return None
    root = TreeNode(a[0])
    q = [root]
    i = 1
    qi = 0
    while i < len(a):
        node = q[qi]
        qi += 1
        if i < len(a) and a[i] is not None:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1
        if i < len(a) and a[i] is not None:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1
    return root


def dump_tree(root, limit=200000):
    if root is None:
        return []
    out = []
    q = [root]
    qi = 0
    seen = 0
    while qi < len(q):
        node = q[qi]
        qi += 1
        if node is None:
            out.append(None)
            continue
        if not isinstance(node, TreeNode):
            raise Rejected(f'Arborele contine un obiect care nu e TreeNode: {node!r}')
        seen += 1
        if seen > limit:
            raise Rejected('Arborele returnat are un ciclu (sau e prea mare).')
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_val(root, v):
    st = [root]
    while st:
        n = st.pop()
        if n is None:
            continue
        if n.val == v:
            return n
        st.append(n.left)
        st.append(n.right)
    return None


def build_graph(adj):
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nb in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nb]
    return nodes[0]


def graph_nodes(start):
    seen = {}
    st = [start]
    while st:
        n = st.pop()
        if n is None or id(n) in seen:
            continue
        seen[id(n)] = n
        st.extend(n.neighbors)
    return list(seen.values())


def dump_graph(start):
    if start is None:
        return []
    nodes = graph_nodes(start)
    by_val = {n.val: n for n in nodes}
    if len(by_val) != len(nodes):
        raise Rejected('Graful clonat are mai multe noduri cu aceeasi valoare.')
    return [[m.val for m in by_val[v].neighbors] for v in range(1, len(nodes) + 1)]


CONV_IN = {
    'raw': lambda a: a,
    'list': build_list,
    'lists': lambda a: [build_list(x) for x in a],
    'tree': build_tree,
}
CONV_OUT = {
    'raw': lambda r: r,
    'list': dump_list,
    'tree': dump_tree,
    'val': lambda n: None if n is None else n.val,
}


def plain(x):
    """tuple -> list, set -> lista sortata, recursiv; ca sa arate ca JSON."""
    if isinstance(x, (list, tuple)):
        return [plain(v) for v in x]
    if isinstance(x, (set, frozenset)):
        try:
            return sorted(plain(v) for v in x)
        except TypeError:
            return [plain(v) for v in x]
    if isinstance(x, dict):
        return {k: plain(v) for k, v in x.items()}
    if isinstance(x, float) and x.is_integer() and abs(x) < 2 ** 53:
        return x
    return x


def dismantle(objs):
    """Desface iterativ legaturile dintre noduri. Pyodide umple stiva JS cand elibereaza
    recursiv o lista inlantuita de cateva mii de noduri, asa ca le taiem noi inainte."""
    st = list(objs)
    seen = set()
    while st:
        x = st.pop()
        if isinstance(x, (list, tuple)):
            st.extend(x)
            continue
        if not isinstance(x, (ListNode, TreeNode, Node)) or id(x) in seen:
            continue
        seen.add(id(x))
        if isinstance(x, ListNode):
            st.append(x.next)
            x.next = None
        elif isinstance(x, TreeNode):
            st.append(x.left)
            st.append(x.right)
            x.left = x.right = None
        else:
            st.append(x.neighbors)
            x.neighbors = []


# ---------- rulare ----------
def run_case(ns, spec, args):
    keep = []
    try:
        return _run_case(ns, spec, copy.deepcopy(args), keep)
    finally:
        dismantle(keep)
        keep.clear()


def _run_case(ns, spec, args, keep):
    mode = spec.get('mode', 'func')

    if mode == 'design':
        ops, params = args
        cls = ns.get(ops[0])
        if cls is None:
            raise NameError(f'Clasa {ops[0]} nu e definita.')
        obj = cls(*params[0])
        out = [None]
        for op, p in zip(ops[1:], params[1:]):
            out.append(getattr(obj, op)(*p))
        return plain(out)

    if mode == 'codec':
        root = build_tree(args[0])
        keep.append(root)
        ser = ns['Codec']()
        de = ns['Codec']()
        data = ser.serialize(root)
        if not isinstance(data, str):
            raise Rejected(f'serialize trebuie sa returneze un str, nu {type(data).__name__}.')
        res = de.deserialize(data)
        keep.append(res)
        return dump_tree(res)

    sol = ns['Solution']()
    fn = getattr(sol, spec['fn'])

    if mode == 'cycle':
        values, pos = args
        head = build_list(values)
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        keep.append(nodes)
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        res = fn(head)
        keep.append(res)
        if spec.get('ret') == 'index':
            if res is None:
                return -1
            for i, n in enumerate(nodes):
                if n is res:
                    return i
            raise Rejected('Nodul returnat nu face parte din lista.')
        return plain(res)

    if mode == 'lca':
        root = build_tree(args[0])
        p = find_val(root, args[1])
        q = find_val(root, args[2])
        keep.append(root)
        res = fn(root, p, q)
        return None if res is None else res.val

    if mode == 'clone':
        start = build_graph(args[0])
        orig = {id(n) for n in graph_nodes(start)} if start else set()
        keep.append(graph_nodes(start) if start else [])
        res = fn(start)
        keep.append(graph_nodes(res) if isinstance(res, Node) else res)
        if res is not None and any(id(n) in orig for n in graph_nodes(res)):
            raise Rejected('Clona refoloseste noduri din graful original.')
        return dump_graph(res)

    types = spec.get('types', [])
    conv = [CONV_IN[types[i] if i < len(types) else 'raw'](a) for i, a in enumerate(args)]
    if any(t != 'raw' for t in types):
        keep.append(conv)
    res = fn(*conv)
    keep.append(res)
    if 'inplace' in spec:
        i = spec['inplace']
        res = CONV_OUT[types[i] if i < len(types) else 'raw'](conv[i])
        return plain(res)
    if spec.get('check') == 'kprefix':
        return [res, plain(conv[0][:res]) if isinstance(res, int) else None]
    return plain(CONV_OUT[spec.get('ret', 'raw')](res))


def _sort(x):
    try:
        return sorted(x)
    except TypeError:
        return sorted(x, key=repr)


def _round(x):
    if isinstance(x, list):
        return [_round(v) for v in x]
    if isinstance(x, (int, float)) and not isinstance(x, bool):
        return round(float(x), 5) + 0.0
    return x


def canon(spec, x):
    c = spec.get('check', 'exact')
    if c == 'float':
        return _round(x)
    if not isinstance(x, list):
        return x
    if c == 'sort':
        return _sort(x)
    if c == 'sort_deep':
        return _sort([_sort(v) if isinstance(v, list) else v for v in x])
    return x


def digest(spec, x):
    s = json.dumps(canon(spec, x), separators=(',', ':'), sort_keys=True)
    return hashlib.sha256(s.encode()).hexdigest()[:24]


def close(a, b):
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(close(x, y) for x, y in zip(a, b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool):
        return math.isclose(a, b, rel_tol=1e-5, abs_tol=1e-5)
    return a == b


def valid_topo(n, pre, order):
    if not isinstance(order, list):
        return False
    if not order:
        return None  # decis de expected
    if sorted(order) != list(range(n)):
        return False
    pos = {v: i for i, v in enumerate(order)}
    return all(pos[b] < pos[a] for a, b in pre)


def check(spec, got, exp, args):
    c = spec.get('check', 'exact')
    if c == 'float':
        return close(got, exp)
    if c == 'palindrome':
        s = args[0]
        return isinstance(got, str) and got == got[::-1] and got in s and len(got) == len(exp)
    if c == 'topo':
        v = valid_topo(args[0], args[1], got)
        return (exp == []) if v is None else (v and exp != [])
    if c == 'window':
        if not isinstance(got, str) or len(got) != len(exp):
            return False
        if not exp:
            return True
        have = collections.Counter(got)
        return got in args[0] and all(have[ch] >= k for ch, k in collections.Counter(args[1]).items())
    if c == 'gas':
        if exp == -1 or got == -1:
            return got == exp
        gas, cost = args
        n = len(gas)
        if not isinstance(got, int) or not 0 <= got < n:
            return False
        tank = 0
        for i in range(n):
            j = (got + i) % n
            tank += gas[j] - cost[j]
            if tank < 0:
                return False
        return True
    return canon(spec, got) == canon(spec, exp)


# ---------- API folosit de worker ----------
_ns = None


def prepare(code):
    """Compileaza codul utilizatorului. Returneaza None sau mesajul de eroare."""
    global _ns
    ns = {'__name__': '__solution__', 'ListNode': ListNode, 'TreeNode': TreeNode, 'Node': Node}
    exec(PRELUDE, ns)
    linecache.cache['solution.py'] = (len(code), None, code.splitlines(True), 'solution.py')
    try:
        exec(compile(code, 'solution.py', 'exec'), ns)
    except BaseException:
        _ns = None
        return user_traceback()
    _ns = ns
    return None


def user_traceback():
    et, ev, tb = sys.exc_info()
    frames = [f for f in traceback.extract_tb(tb) if f.filename == 'solution.py']
    lines = ''.join(traceback.format_list(frames)) if frames else ''
    msg = ''.join(traceback.format_exception_only(et, ev))
    if lines:
        return 'Traceback (most recent call last):\n' + lines + msg
    return msg


def gen_args(gen, seed):
    env = {'r': random.Random(seed), 'random': random}
    exec(gen, env)
    return env['args']


def show(x, limit=4000):
    s = json.dumps(x, separators=(',', ':'), ensure_ascii=False)
    return s if len(s) <= limit else s[:limit] + ' …'


def run_one(spec_json, test_json):
    spec = json.loads(spec_json)
    test = json.loads(test_json)
    if 'gen' in test:
        args = gen_args(test['gen'], test['seed'])
    else:
        args = test['input']
    out = io.StringIO()
    old = sys.stdout
    sys.stdout = out
    t0 = time.perf_counter()
    res = {}
    try:
        got = run_case(_ns, spec, args)
        res['time'] = round((time.perf_counter() - t0) * 1000, 1)
        if 'hash' in test:
            ok = digest(spec, got) == test['hash']
        else:
            ok = check(spec, got, test['expected'], args)
        res['status'] = 'ok' if ok else 'wrong'
        res['output'] = show(got)
    except Rejected as e:
        res['status'] = 'wrong'
        res['output'] = str(e)
    except BaseException:
        res['status'] = 'error'
        res['error'] = user_traceback()
    finally:
        sys.stdout = old
    res['stdout'] = out.getvalue()[-4000:]
    return json.dumps(res)


def run_raw(spec_json, args_json):
    """Ruleaza pe un input scris de utilizator, fara rezultat asteptat."""
    spec = json.loads(spec_json)
    out = io.StringIO()
    old = sys.stdout
    sys.stdout = out
    res = {}
    try:
        got = run_case(_ns, spec, json.loads(args_json))
        res['status'] = 'done'
        res['output'] = show(got)
    except Rejected as e:
        res['status'] = 'wrong'
        res['output'] = str(e)
    except BaseException:
        res['status'] = 'error'
        res['error'] = user_traceback()
    finally:
        sys.stdout = old
    res['stdout'] = out.getvalue()[-4000:]
    return json.dumps(res)
