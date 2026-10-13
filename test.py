#!/usr/bin/env python3
"""Ruleaza testele de pe site pe solutiile din Probleme/.

    python3 test.py 1                 problema nr. 1 (Two Sum)
    python3 test.py two-sum           dupa nume (ajunge si o bucata din el)
    python3 test.py Probleme/01-hashing/1.two-sum.py
    python3 test.py hashing           toate problemele unui tipar (sau calea folderului)
    python3 test.py                   toate problemele la care ai scris ceva
    python3 test.py 1 -e              doar exemplele, cu output-ul afisat (ca „Rulează” pe site)
    python3 test.py -l                lista problemelor si unde ai ramas

Fara -e ruleaza toate testele, inclusiv cele mari (ca „Trimite” pe site). Limitele de timp sunt
cele de pe site: 3 secunde pe un test obisnuit, 6 pe unul mare.
"""
import argparse
import hashlib
import json
import os
import queue
import re
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOL = ROOT / 'Probleme'
DATA = ROOT / '_teste' / 'teste.json'
STATE = ROOT / '_teste' / '.rezultate.json'
TL_SMALL, TL_BIG = 3.0, 6.0
TL_LOAD = 10.0
SHOW = 600
MAX_DETAILS = 3

COLOR = sys.stdout.isatty() and 'NO_COLOR' not in os.environ


def paint(code, s):
    return f'\033[{code}m{s}\033[0m' if COLOR else s


def green(s): return paint('32', s)
def red(s): return paint('31', s)
def yellow(s): return paint('33', s)
def dim(s): return paint('2', s)
def bold(s): return paint('1', s)


VERDICT = {'wrong': 'Wrong Answer', 'error': 'Runtime Error', 'tle': 'Time Limit Exceeded'}
DIFF = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}


def load():
    if not DATA.is_file():
        raise SystemExit('Lipsește _teste/teste.json. Rulează: python3 _teste/sync.py')
    with open(DATA, encoding='utf-8') as f:
        return json.load(f)


# ---------- procesul copil: ruleaza solutia si raporteaza dupa fiecare test ----------
def worker(fd, path, slug, only_ex):
    sys.path.insert(0, str(ROOT))
    from _teste import harness
    out = os.fdopen(int(fd), 'w')

    def send(**m):
        out.write(json.dumps(m) + '\n')
        out.flush()

    P = next(p for p in load()['problems'] if p['slug'] == slug)
    tests = P['tests'][:P['ex']] if only_ex == '1' else P['tests']
    err = harness.prepare(Path(path).read_text(encoding='utf-8'))
    if err:
        send(t='compile', error=err)
        return
    spec = json.dumps(P['spec'])
    for i, t in enumerate(tests):
        send(t='start', i=i)
        send(t='result', i=i, r=json.loads(harness.run_one(spec, json.dumps(t))))
    send(t='done')


def run_problem(P, path, only_ex):
    """Ruleaza testele intr-un proces separat, ca sa-l putem opri la Time Limit Exceeded."""
    tests = P['tests'][:P['ex']] if only_ex else P['tests']
    r, w = os.pipe()
    proc = subprocess.Popen([sys.executable, '-B', str(ROOT / 'test.py'), '--worker', str(w), str(path), P['slug'],
                             '1' if only_ex else '0'], pass_fds=[w])
    os.close(w)
    q = queue.Queue()

    def reader():
        with os.fdopen(r) as f:
            for line in f:
                q.put(json.loads(line))
        q.put(None)

    threading.Thread(target=reader, daemon=True).start()
    res = {'compile': None, 'results': [None] * len(tests)}
    cur, limit = None, TL_LOAD
    try:
        while True:
            try:
                m = q.get(timeout=limit)
            except queue.Empty:
                proc.kill()
                if cur is None:
                    res['compile'] = f'Fișierul nu s-a încărcat în {TL_LOAD:.0f} secunde (buclă infinită în afara funcției?).'
                else:
                    res['results'][cur] = {'status': 'tle'}
                break
            if m is None:
                code = proc.wait()
                msg = f'Procesul Python s-a oprit (cod {code}): de obicei recursivitate prea adâncă sau prea multă memorie.'
                if cur is None:
                    res['compile'] = msg
                elif res['results'][cur] is None:
                    res['results'][cur] = {'status': 'error', 'error': msg}
                break
            if m['t'] == 'compile':
                res['compile'] = m['error']
                break
            elif m['t'] == 'start':
                cur = m['i']
                limit = TL_BIG if 'gen' in tests[cur] else TL_SMALL
            elif m['t'] == 'result':
                res['results'][m['i']] = m['r']
                limit = TL_LOAD
            elif m['t'] == 'done':
                break
    except KeyboardInterrupt:
        proc.kill()
        raise
    finally:
        proc.wait()
    return res


# ---------- fisiere ----------
def user_code(src):
    m = re.search(r'^# @lc code=start[^\n]*\n(.*?)^# @lc code=end', src, re.S | re.M)
    return m.group(1) if m else src


def norm(s):
    return '\n'.join(line.rstrip() for line in s.strip().splitlines())


def started(P, path):
    return norm(user_code(path.read_text(encoding='utf-8'))) != norm(P['starter'])


def code_hash(path):
    return hashlib.sha1(norm(user_code(path.read_text(encoding='utf-8'))).encode()).hexdigest()[:16]


def solution_files(by_slug):
    out = {}
    for p in sorted(SOL.rglob('*.py')):
        m = re.match(r'\d+\.(.+)\.py$', p.name)
        if m and m.group(1) in by_slug:
            out[m.group(1)] = p
    return out


def rel(path):
    try:
        return os.path.relpath(path)
    except ValueError:
        return str(path)


def resolve(arg, data, by_slug, files):
    """Argument din linia de comanda -> lista de (slug, fisier)."""
    p = Path(arg)
    if p.is_dir():
        inside = [(s, f) for s, f in files.items() if p.resolve() in f.resolve().parents]
        if not inside:
            raise SystemExit(f'Nicio problemă în {arg}.')
        return inside
    if p.is_file():
        m = re.match(r'\d+\.(.+)\.py$', p.name)
        if not m or m.group(1) not in by_slug:
            raise SystemExit(f'Nu știu ce problemă e {arg}. Numele trebuie să fie <număr>.<slug>.py, de ex. 1.two-sum.py.')
        return [(m.group(1), p)]
    key = arg.lower().strip()
    slugs = [s for s, P in by_slug.items() if key.isdigit() and P['n'] == int(key)]
    if not slugs and key in by_slug:
        slugs = [key]
    if not slugs:
        slugs = [P['slug'] for pat in data['patterns'] if key in (pat['id'], pat['dir']) for P in data['problems'] if P['pattern'] == pat['id']]
    if not slugs:
        slugs = [s for s, P in by_slug.items() if key in s or key in P['title'].lower()]
        if len(slugs) > 1:
            names = '\n'.join(f'  {by_slug[s]["n"]:>4}  {s}' for s in slugs)
            raise SystemExit(f'„{arg}” se potrivește cu mai multe probleme:\n{names}')
    if not slugs:
        raise SystemExit(f'Nu găsesc nicio problemă pentru „{arg}”. Vezi lista: python3 test.py -l')
    missing = [s for s in slugs if s not in files]
    if missing:
        raise SystemExit(f'Lipsește fișierul pentru {missing[0]}. Îl recreezi cu: python3 _teste/sync.py')
    return [(s, files[s]) for s in slugs]


# ---------- afisare ----------
def clip(s):
    return s if len(s) <= SHOW else s[:SHOW] + ' …'


def js(v):
    return json.dumps(v, separators=(',', ':'), ensure_ascii=False)


def label(P, i):
    if i < P['ex']:
        return f'Exemplul {i + 1}'
    return f'Testul {i + 1}' + (' (mare)' if 'gen' in P['tests'][i] else '')


def field(name, text):
    lines = text.rstrip('\n').split('\n')
    pad = ' ' * 16
    print(f'     {name + ":":<11}{lines[0]}')
    for line in lines[1:]:
        print(pad + line)


def details(P, i, r, path):
    t = P['tests'][i]
    head = f'{label(P, i)} · ' + ('OK' if r['status'] == 'ok' else VERDICT[r['status']])
    print('\n  ' + bold(head))
    if 'gen' in t:
        field('Input', f'generat, {t["note"]}')
    else:
        field('Input', clip(', '.join(f'{n} = {js(a)}' for n, a in zip(P['params'], t['input']))))
    if r['status'] == 'tle':
        field('Output', f'Peste {TL_BIG if "gen" in t else TL_SMALL:.0f} secunde. Caută o soluție cu complexitate mai mică (sau o buclă infinită).')
        return
    if r['status'] == 'error':
        field('Eroare', r['error'].replace('File "solution.py"', f'File "{rel(path)}"'))
    else:
        field('Output', clip(r['output']))
        field('Expected', clip(js(t['expected'])) if 'expected' in t else 'prea mare ca să fie afișat (se compară prin hash)')
    if r.get('stdout'):
        field('Stdout', r['stdout'])


def summary(P, res):
    """(acceptat, trecute, total, primul verdict prost)"""
    rs = res['results']
    passed = sum(1 for r in rs if r and r['status'] == 'ok')
    if res['compile']:
        return False, 0, len(rs), 'Eroare la încărcare'
    bad = next((VERDICT[r['status']] for r in rs if r and r['status'] != 'ok'), None)
    return passed == len(rs), passed, len(rs), bad


def title(P):
    return f'{P["n"]}. {P["title"]}'


def report_full(P, path, res, only_ex):
    print(bold(title(P)) + dim(f'  ·  {DIFF[P["diff"]]}  ·  {rel(path)}'))
    if res['compile']:
        print(red('\n  Eroare la încărcarea fișierului'))
        print('\n'.join('  ' + line for line in res['compile'].replace('File "solution.py"', f'File "{rel(path)}"').rstrip().split('\n')))
        return
    rs = res['results']
    for i, r in enumerate(rs):
        name = f'{label(P, i):<20}'
        if r is None:
            print(dim(f'  – {name} nerulat'))
        elif r['status'] == 'ok':
            print(green('  ✓ ') + name + dim(f' {r["time"]:.0f} ms'))
        else:
            print(red(f'  ✗ {name} {VERDICT[r["status"]]}'))
    shown, errors = [], set()  # aceeasi eroare pe mai multe teste se arata o singura data
    for i, r in enumerate(rs):
        if r and (only_ex or (r['status'] != 'ok' and r.get('error') not in errors)):
            shown.append(i)
            errors.add(r.get('error', i))
    for i in shown[:len(shown) if only_ex else MAX_DETAILS]:
        details(P, i, rs[i], path)
    if not only_ex and len(shown) > MAX_DETAILS:
        print(dim(f'\n  … și încă {len(shown) - MAX_DETAILS} picate'))
    ok, passed, total, bad = summary(P, res)
    if P['notes'] and any(r and r['status'] == 'wrong' for r in rs):
        print()
        for note in P['notes']:
            print(dim('  Notă: ' + note))
    ms = sum(r.get('time', 0) for r in rs if r)
    what = 'exemple' if only_ex else 'teste'
    print()
    if ok:
        print(green(bold('  Accepted' if not only_ex else '  Exemplele trec')) + f'  {passed}/{total} {what}, {ms:.0f} ms')
        if only_ex:
            print(dim(f'  Toate testele: python3 test.py {P["n"]}'))
    else:
        print(red(bold(f'  {bad}')) + f'  {passed}/{total} {what} trecute')


def report_line(P, res):
    ok, passed, total, bad = summary(P, res)
    mark = green('✓') if ok else red('✗')
    tail = dim(f'{passed}/{total}') if ok else red(f'{passed}/{total}  {bad}')
    print(f'{mark} {P["n"]:>4}  {P["title"]:<58} {tail}')


def show_list(data, by_slug, files):
    state = read_state()
    done = begun = 0
    for pat in data['patterns']:
        print('\n' + bold(f'{pat["dir"]}  {pat["name"]}'))
        for P in data['problems']:
            if P['pattern'] != pat['id']:
                continue
            f = files.get(P['slug'])
            st = state.get(P['slug'])
            if f is None:
                mark, note = dim('?'), dim('lipsește fișierul')
            elif not started(P, f):
                mark, note = dim('○'), ''
            elif st and st['h'] == code_hash(f):
                mark = green('✓') if st['ok'] else red('✗')
                note = '' if st['ok'] else red(f'{st["p"]}/{st["t"]} teste')
                done += st['ok']
                begun += 1
            else:
                mark, note = yellow('●'), dim('netestată de la ultima modificare')
                begun += 1
            print(f'  {mark} {P["n"]:>4}  {P["title"]:<58} {DIFF[P["diff"]]:<7} {note}')
    total = len(data['problems'])
    print(f'\n{green("✓")} acceptate: {done}/{total}   {yellow("●")} începute: {begun}   {dim("○")} neîncepute: {total - begun}')


def read_state():
    try:
        return json.loads(STATE.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return {}


def save_state(slug, path, res, P):
    if SOL.resolve() not in path.resolve().parents:
        return
    ok, passed, total, _ = summary(P, res)
    state = read_state()
    state[slug] = {'h': code_hash(path), 'ok': ok, 'p': passed, 't': total}
    STATE.write_text(json.dumps(state, indent=0, sort_keys=True), encoding='utf-8')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('ce', nargs='*', help='număr, nume, fișier, folder sau tipar; fără nimic = tot ce ai început')
    ap.add_argument('-e', '--exemple', action='store_true', help='doar exemplele, cu output-ul afișat')
    ap.add_argument('-l', '--lista', action='store_true', help='lista problemelor și unde ai rămas')
    args = ap.parse_args(argv)

    data = load()
    by_slug = {P['slug']: P for P in data['problems']}
    files = solution_files(by_slug)
    if args.lista:
        show_list(data, by_slug, files)
        return 0

    if args.ce:
        todo = [x for a in args.ce for x in resolve(a, data, by_slug, files)]
    else:
        todo = [(s, files[s]) for s in by_slug if s in files]
    one = len(todo) == 1
    skipped = 0
    if not one:
        skipped = sum(1 for s, f in todo if not started(by_slug[s], f))
        todo = [(s, f) for s, f in todo if started(by_slug[s], f)]
        if not todo:
            print('Nicio problemă începută aici. Scrie o soluție în Probleme/ și rulează de ex.: python3 test.py 1')
            return 0

    failed = 0
    for slug, path in todo:
        P = by_slug[slug]
        if one and not started(P, path):
            print(bold(title(P)) + dim(f'  ·  {rel(path)}'))
            print('\n  Fișierul are doar codul de pornire. Scrie soluția între `# @lc code=start` și `# @lc code=end`.')
            return 1
        res = run_problem(P, path, args.exemple)
        if not args.exemple:
            save_state(slug, path, res, P)
        (report_full(P, path, res, args.exemple) if one else report_line(P, res))
        failed += not summary(P, res)[0]
    if not one:
        print(f'\n{len(todo) - failed}/{len(todo)} acceptate' + (dim(f'   ({skipped} neîncepute, sărite)') if skipped else ''))
    return 1 if failed else 0


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--worker':
        worker(*sys.argv[2:])
    else:
        try:
            sys.exit(main())
        except KeyboardInterrupt:
            sys.exit(130)
