#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#
# Medium  ·  Topological Sort
# https://leetcode.com/problems/find-eventual-safe-states/
#
# Ai un graf orientat cu `n` noduri, numerotate de la 0 la `n − 1`, dat ca listă de adiacență:
# `graph[i]` conține nodurile spre care există muchie din nodul `i`.
#
# Un nod e terminal dacă nu are muchii care ies din el. Un nod e sigur dacă orice drum care
# pornește din el ajunge într-un nod terminal (sau în alt nod sigur).
#
# Returnează toate nodurile sigure, sortate crescător.
#
# Exemplul 1
#   Input:  graph = [[1,2],[2,3],[5],[0],[5],[],[]]
#   Output: [2,4,5,6]
#
# Exemplul 2
#   Input:  graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
#   Output: [4]
#
# Constrângeri:
#   - `n == len(graph)`
#   - `1 ≤ n ≤ 10⁴`
#   - `0 ≤ len(graph[i]) ≤ n`
#   - `0 ≤ graph[i][j] ≤ n − 1`
#   - `graph[i]` e sortat strict crescător
#   - Graful poate conține bucle (muchii de la un nod la el însuși)
#   - Numărul de muchii e în intervalul `[1, 4 · 10⁴]`
#
# Teste:  python3 test.py 802      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
# @lc code=end
