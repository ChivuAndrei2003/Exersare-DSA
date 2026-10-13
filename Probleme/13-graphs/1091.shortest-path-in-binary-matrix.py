#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
#
# Primești o matrice binară `grid` de n × n. Returnează lungimea celui mai scurt drum liber din
# matrice sau −1 dacă nu există niciunul.
#
# Un drum liber pleacă din celula stânga-sus `(0, 0)`, ajunge în celula dreapta-jos `(n − 1, n −
# 1)`, trece doar prin celule cu valoarea 0, iar celulele consecutive sunt vecine pe 8 direcții
# (au o latură sau un colț comun).
#
# Lungimea drumului e numărul de celule vizitate.
#
# Exemplul 1
#   Input:  grid = [[0,1],[1,0]]
#   Output: 2
#
# Exemplul 2
#   Input:  grid = [[0,0,0],[1,1,0],[1,1,0]]
#   Output: 4
#
# Exemplul 3
#   Input:  grid = [[1,0,0],[1,1,0],[1,1,0]]
#   Output: -1
#
# Constrângeri:
#   - `n == len(grid) == len(grid[i])`
#   - `1 ≤ n ≤ 100`
#   - `grid[i][j]` e 0 sau 1
#
# Teste:  python3 test.py 1091      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
# @lc code=end
