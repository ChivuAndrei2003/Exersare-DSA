#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# Medium  ·  Topological Sort
# https://leetcode.com/problems/minimum-height-trees/
#
# Un arbore e un graf neorientat în care oricare două noduri sunt legate printr-un singur drum (un
# graf conex, fără cicluri). Primești un arbore cu `n` noduri, numerotate de la 0 la `n − 1`, și
# lista celor `n − 1` muchii, `edges[i] = [a, b]`.
#
# Poți alege orice nod ca rădăcină. Înălțimea arborelui cu rădăcina aleasă e numărul de muchii de
# pe cel mai lung drum de la rădăcină la o frunză. Arborii cu înălțimea minimă posibilă se numesc
# arbori de înălțime minimă (MHT).
#
# Returnează lista rădăcinilor tuturor MHT-urilor, în orice ordine.
#
# Exemplul 1
#   Input:  n = 4, edges = [[1,0],[1,2],[1,3]]
#   Output: [1]
#
# Exemplul 2
#   Input:  n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#   Output: [3,4]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ n ≤ 2 · 10⁴`
#   - `len(edges) == n − 1`
#   - `0 ≤ a, b < n`
#   - `a ≠ b`
#   - Toate perechile `(a, b)` sunt distincte
#   - Inputul e garantat un arbore, fără muchii repetate
#
# Teste:  python3 test.py 310      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
# @lc code=end
