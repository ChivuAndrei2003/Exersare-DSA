#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#
# Easy  ·  Union-Find (DSU)
# https://leetcode.com/problems/find-if-path-exists-in-graph/
#
# Ai un graf neorientat cu `n` noduri, numerotate de la 0 la `n − 1`. Muchiile sunt date în
# `edges`, unde `edges[i] = [u, v]` e o muchie între `u` și `v`. Între două noduri există cel mult
# o muchie și niciun nod nu are muchie către el însuși.
#
# Returnează `True` dacă există un drum de la nodul `source` la nodul `destination` și `False`
# altfel.
#
# Exemplul 1
#   Input:  n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
#   Output: true
#
# Exemplul 2
#   Input:  n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
#   Output: false
#
# Constrângeri:
#   - `1 ≤ n ≤ 2 · 10⁵`
#   - `0 ≤ len(edges) ≤ 2 · 10⁵`
#   - `len(edges[i]) == 2`
#   - `0 ≤ u, v ≤ n − 1`
#   - `u ≠ v`
#   - `0 ≤ source, destination ≤ n − 1`
#   - Fără muchii duplicate și fără bucle
#
# Teste:  python3 test.py 1971      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
# @lc code=end
