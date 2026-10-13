#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# Medium  ·  Linked List
# https://leetcode.com/problems/lru-cache/
#
# Proiectează un LRU cache (Least Recently Used): un cache cu capacitate fixă care, atunci când se
# umple, evacuează cheia folosită cel mai de demult.
#
# Implementează clasa `LRUCache`. `LRUCache(capacity)` creează cache-ul, cu o capacitate pozitivă.
# `get(key)` returnează valoarea cheii sau −1 dacă nu există. `put(key, value)` actualizează
# valoarea dacă cheia există; altfel adaugă perechea, iar dacă numărul de chei depășește
# capacitatea, evacuează cheia folosită cel mai de demult.
#
# Atât `get`, cât și `put` contează ca folosire a cheii. Ambele trebuie să ruleze în O(1) în
# medie.
#
# Exemplul 1
#   Input:
#     operations = ["LRUCache","put","put","get","put","get","put","get","get","get"]
#     arguments = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
#   Output: [null,null,null,1,null,-1,null,-1,3,4]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `1 ≤ capacity ≤ 3000`
#   - `0 ≤ key ≤ 10⁴`
#   - `0 ≤ value ≤ 10⁵`
#   - Cel mult 2 · 10⁵ apeluri către `get` și `put`
#
# Teste:  python3 test.py 146      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):


    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:
        
# @lc code=end
