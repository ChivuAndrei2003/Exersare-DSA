#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# Medium  ·  Trie
# https://leetcode.com/problems/implement-trie-prefix-tree/
#
# Un trie (arbore de prefixe) e o structură arborescentă folosită pentru a stoca și a căuta
# eficient stringuri — de exemplu la autocomplete și la verificarea ortografică.
#
# Implementează clasa `Trie`. `Trie()` creează obiectul. `insert(word)` inserează stringul `word`.
# `search(word)` returnează `True` dacă `word` a fost inserat înainte și `False` altfel.
# `startsWith(prefix)` returnează `True` dacă există un string inserat care începe cu `prefix` și
# `False` altfel.
#
# Exemplul 1
#   Input:
#     operations = ["Trie","insert","search","search","startsWith","insert","search"]
#     arguments = [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
#   Output: [null,null,true,false,true,null,true]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `1 ≤ len(word), len(prefix) ≤ 2000`
#   - `word` și `prefix` conțin doar litere mici ale alfabetului englez
#   - Cel mult 3 · 10⁴ apeluri în total către `insert`, `search` și `startsWith`
#
# Teste:  python3 test.py 208      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Trie:

    def __init__(self):


    def insert(self, word: str) -> None:


    def search(self, word: str) -> bool:


    def startsWith(self, prefix: str) -> bool:
        
# @lc code=end
