#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/rotting-oranges/
#
# Primești o grilă `grid` de m × n, în care fiecare celulă are una dintre valorile: 0 — celulă
# goală, 1 — portocală proaspătă, 2 — portocală stricată.
#
# În fiecare minut, orice portocală proaspătă vecină pe cele 4 direcții cu una stricată se strică
# și ea.
#
# Returnează numărul minim de minute după care nu mai rămâne nicio portocală proaspătă. Dacă asta
# e imposibil, returnează −1.
#
# Exemplul 1
#   Input:  grid = [[2,1,1],[1,1,0],[0,1,1]]
#   Output: 4
#
# Exemplul 2
#   Input:  grid = [[2,1,1],[0,1,1],[1,0,1]]
#   Output: -1
#
# Exemplul 3
#   Input:  grid = [[0,2]]
#   Output: 0
#
# Constrângeri:
#   - `m == len(grid)`, `n == len(grid[i])`
#   - `1 ≤ m, n ≤ 10`
#   - `grid[i][j]` e 0, 1 sau 2
#
# Teste:  python3 test.py 994      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
# @lc code=end
