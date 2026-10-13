#!/usr/bin/env python3
"""Aduce problemele si testele de pe site (GhidDSA) in folderul asta.

    python3 _teste/sync.py [cale/spre/GhidDSA]

Rescrie _teste/teste.json, _teste/harness.py si dsa.py. Creeaza in Probleme/ fisierele de
solutie care lipsesc; pe cele care exista deja NU le atinge. Are nevoie de `node`, ca sa
citeasca js/data.js, js/statements.js si js/tests.js.
"""
import json
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
SOL = ROOT / 'Probleme'
WIDTH = 96

DUMP_JS = '''
const path = require('path');
const root = process.argv[1];
global.window = {};
for (const f of ['data', 'statements', 'tests']) require(path.join(root, 'js', f + '.js'));
process.stdout.write(JSON.stringify({
  patterns: window.DSA.PATTERNS.map((p) => ({
    id: p.id,
    name: p.name,
    problems: p.problems.map(({ n, title, slug, diff }) => ({ n, title, slug, diff })),
  })),
  statements: window.DSA_STATEMENTS,
  tests: window.DSA_TESTS,
}));
'''

DIFF = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}

# Aceleasi note ca in pagina „Rezolvă” de pe site (js/solve.js).
SPECIAL = {
    'cycle': 'Inputul listei are și `pos`: indexul nodului în care se leagă coada (−1 = fără ciclu). Funcția ta primește doar `head`.',
    'lca': '`p` și `q` sunt valorile nodurilor; funcția ta primește nodurile propriu-zise și returnează nodul strămoș.',
    'clone': 'Graful e dat ca listă de adiacență (nodul `i + 1` are vecinii `adjList[i]`). Funcția ta primește nodul 1.',
    'codec': 'Se verifică `deserialize(serialize(root))`: trebuie să obții același arbore.',
    'design': 'Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.',
}
CHECK_NOTE = {
    'sort': 'Ordinea elementelor din răspuns nu contează.',
    'sort_deep': 'Ordinea nu contează (nici în listă, nici în interiorul grupurilor).',
    'float': 'Răspunsurile se acceptă cu o eroare de până la 10⁻⁵.',
    'palindrome': 'Dacă sunt mai multe răspunsuri corecte, oricare e acceptat.',
    'window': 'Dacă sunt mai multe ferestre minime, oricare e acceptată.',
    'topo': 'Orice ordine validă e acceptată.',
    'kprefix': 'Se verifică `k` și primele `k` elemente din `nums` după apel.',
    'gas': 'Orice stație de start validă e acceptată.',
}
INPLACE_NOTE = 'Funcția modifică inputul pe loc; se verifică inputul după apel.'


def notes_for(spec):
    out = []
    if spec.get('mode') in SPECIAL:
        out.append(SPECIAL[spec['mode']])
    if spec.get('check') in CHECK_NOTE:
        out.append(CHECK_NOTE[spec['check']])
    if 'inplace' in spec:
        out.append(INPLACE_NOTE)
    return out


def strip_md(s):
    """Scoate **bold** si *italic*, dar lasa `codul` neatins."""
    parts = s.split('`')
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r'\*\*(.+?)\*\*', r'\1', parts[i])
        parts[i] = re.sub(r'(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])', r'\1', parts[i])
    return '`'.join(parts)


def wrap(s, indent=''):
    return textwrap.wrap(strip_md(s), WIDTH - len(indent), initial_indent=indent,
                         subsequent_indent=indent, break_long_words=False, break_on_hyphens=False)


def js(v):
    return json.dumps(v, separators=(',', ':'), ensure_ascii=False)


def value_lines(label, v, indent):
    """`label = valoare`, cu matricele mari sparte pe randuri."""
    s = js(v)
    if len(indent) + len(label) + len(s) <= WIDTH or not (isinstance(v, list) and v and all(isinstance(r, list) for r in v)):
        return [f'{indent}{label}{s}']
    pad = indent + '  '
    return [f'{indent}{label}['] + [f'{pad}{js(r)},' for r in v[:-1]] + [f'{pad}{js(v[-1])}', f'{indent}]']


def example_lines(P, t):
    pairs = [f'{name} = {js(a)}' for name, a in zip(P['params'], t['input'])]
    inline = '  Input:  ' + ', '.join(pairs)
    if len(inline) <= WIDTH:
        out = [inline]
    else:
        out = ['  Input:']
        for name, a in zip(P['params'], t['input']):
            out += value_lines(f'{name} = ', a, '    ')
    return out + value_lines('Output: ', t['expected'], '  ')


def solution_file(pr, pattern, P, st):
    L = ['', f'@lc app=leetcode id={pr["n"]} lang=python3', '', f'[{pr["n"]}] {pr["title"]}', '',
         f'{DIFF[pr["diff"]]}  ·  {pattern["name"]}', f'https://leetcode.com/problems/{pr["slug"]}/', '']
    for para in st.get('text', []):
        L += wrap(para) + ['']
    for i, t in enumerate(P['tests'][:P['ex']]):
        L += [f'Exemplul {i + 1}'] + example_lines(P, t) + ['']
    for note in notes_for(P['spec']):
        L += wrap('Notă: ' + note) + ['']
    if st.get('cons'):
        L.append('Constrângeri:')
        for c in st['cons']:
            w = wrap(c, '    ')
            L += ['  - ' + w[0].lstrip()] + w[1:]
        L.append('')
    L += [f'Teste:  python3 test.py {pr["n"]}      (în VS Code: Cmd+Shift+B)', '']
    head = '\n'.join(('# ' + line).rstrip() for line in L)
    starter = P['starter'].rstrip('\n')
    if starter.endswith(':'):  # clasele de design: loc de scris si sub ultima metoda
        starter += '\n        '
    return (f'{head}\n'
            'from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...\n'
            '\n'
            '# @lc code=start\n'
            f'{starter}\n'
            '# @lc code=end\n')


def dsa_module(prelude):
    return ('"""Ce are LeetCode deja importat. Fisierele din Probleme/ incep cu `from dsa import *`, ca\n'
            'editorul sa cunoasca List, Optional, ListNode, TreeNode, Counter, deque, heappush etc.\n'
            'Linia e in afara blocului `@lc code`, deci nu ajunge pe LeetCode. Testele (test.py) dau\n'
            'aceleasi nume si fara ea. Generat de _teste/sync.py din _teste/harness.py."""\n'
            f'{prelude.strip()}\n'
            'from _teste.harness import ListNode, TreeNode, Node\n')


def main():
    site = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else ROOT.parent / 'GhidDSA'
    if not (site / 'js' / 'tests.js').is_file():
        raise SystemExit(f'Nu gasesc site-ul in {site}. Da calea: python3 _teste/sync.py cale/spre/GhidDSA')
    dump = json.loads(subprocess.run(['node', '-e', DUMP_JS, str(site)], check=True, capture_output=True, text=True).stdout)

    shutil.copyfile(site / 'py' / 'harness.py', ROOT / '_teste' / 'harness.py')
    sys.path.insert(0, str(ROOT))
    from _teste import harness
    (ROOT / 'dsa.py').write_text(dsa_module(harness.PRELUDE), encoding='utf-8')

    existing = {}
    for p in SOL.rglob('*.py'):
        m = re.match(r'\d+\.(.+)\.py$', p.name)
        if m:
            existing[m.group(1)] = p

    patterns, problems, created = [], [], 0
    for i, pat in enumerate(dump['patterns'], 1):
        d = f'{i:02d}-{pat["id"]}'
        patterns.append({'id': pat['id'], 'name': pat['name'], 'dir': d})
        for pr in pat['problems']:
            slug = pr['slug']
            P = dump['tests'][slug]
            path = existing.get(slug)
            if path is None:
                path = SOL / d / f'{pr["n"]}.{slug}.py'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(solution_file(pr, pat, P, dump['statements'].get(slug, {})), encoding='utf-8')
                created += 1
            problems.append({**pr, 'pattern': pat['id'], 'notes': notes_for(P['spec']), **P})

    with open(ROOT / '_teste' / 'teste.json', 'w', encoding='utf-8') as f:
        f.write('{"patterns":' + js(patterns) + ',\n"problems":[\n')
        f.write(',\n'.join(js(p) for p in problems))
        f.write('\n]}\n')
    n_tests = sum(len(p['tests']) for p in problems)
    print(f'{len(problems)} probleme, {n_tests} teste -> _teste/teste.json')
    print(f'{created} fisiere noi in Probleme/, {len(problems) - created} existente lasate neatinse')


if __name__ == '__main__':
    main()
