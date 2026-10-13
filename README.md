# Exersare DSA

Cele 148 de probleme de pe [GhidDSA](https://ghiddsaplatforma.vercel.app), câte un fișier pentru fiecare, plus testele de pe site ca să le poți verifica local.

## Cum lucrezi

1. Deschide fișierul problemei din `Probleme/<tipar>/`, de exemplu `Probleme/01-hashing/1.two-sum.py`. Sus ai enunțul, exemplele și constrângerile.
2. Scrie soluția între `# @lc code=start` și `# @lc code=end`.
3. Rulează testele:

```bash
python3 test.py 1
```

În VS Code, **Cmd+Shift+B** testează fișierul deschis.

## Comenzi

| Comandă | Ce face |
| --- | --- |
| `python3 test.py 1` | problema nr. 1, toate testele (ca „Trimite” pe site) |
| `python3 test.py two-sum` | la fel, după nume; ajunge și o bucată din el |
| `python3 test.py 1 -e` | doar exemplele, cu output-ul și `print`-urile tale (ca „Rulează”) |
| `python3 test.py hashing` | toate problemele începute dintr-un tipar |
| `python3 test.py` | toate problemele la care ai scris ceva |
| `python3 test.py -l` | lista problemelor: ✓ acceptată, ✗ picată, ● netestată, ○ neîncepută |

Verdictele sunt cele de pe site: Accepted, Wrong Answer, Runtime Error, Time Limit Exceeded (3 secunde pe un test obișnuit, 6 pe unul mare). Python-ul local e mai rapid decât cel din browser, deci o soluție la limită poate trece aici și pica pe site.

## Structură

```
Probleme/         câte un folder pe tipar, în ordinea de pe site; fișierele sunt <număr>.<slug>.py
test.py           rulează testele
dsa.py            ce are LeetCode deja importat (List, ListNode, TreeNode, Counter, deque...)
_teste/           testele (teste.json), harness-ul de pe site și sync.py
Algoritmi/        template-urile tale
```

Fișierele au formatul extensiei LeetCode din VS Code, deci le poți trimite și pe LeetCode direct din editor. Linia `from dsa import *` e în afara blocului `@lc code`, așa că nu ajunge acolo; e doar ca editorul să cunoască `List`, `ListNode` etc.

## Când se schimbă problemele pe site

```bash
python3 _teste/sync.py
```

Reface `_teste/teste.json` din `../GhidDSA` (sau din calea dată ca argument) și creează fișierele problemelor noi. Fișierele care există deja nu sunt atinse.
