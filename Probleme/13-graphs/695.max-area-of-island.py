#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/max-area-of-island/
#
# Primești o grilă binară `grid` de m × n. O insulă e un grup de celule cu valoarea 1 (uscat)
# legate pe cele 4 direcții (orizontal sau vertical). Marginile grilei se consideră înconjurate de
# apă.
#
# Aria unei insule e numărul ei de celule. Returnează aria maximă a unei insule din grilă sau 0
# dacă nu există nicio insulă.
#
# Exemplul 1
#   Input:
#     grid = [
#       [0,0,1,0,0,0,0,1,0,0,0,0,0],
#       [0,0,0,0,0,0,0,1,1,1,0,0,0],
#       [0,1,1,0,1,0,0,0,0,0,0,0,0],
#       [0,1,0,0,1,1,0,0,1,0,1,0,0],
#       [0,1,0,0,1,1,0,0,1,1,1,0,0],
#       [0,0,0,0,0,0,0,0,0,0,1,0,0],
#       [0,0,0,0,0,0,0,1,1,1,0,0,0],
#       [0,0,0,0,0,0,0,1,1,0,0,0,0]
#     ]
#   Output: 6
#
# Exemplul 2
#   Input:  grid = [[0,0,0,0,0,0,0,0]]
#   Output: 0
#
# Constrângeri:
#   - `m == len(grid)`, `n == len(grid[i])`
#   - `1 ≤ m, n ≤ 50`
#   - `grid[i][j]` e 0 sau 1
#
# Teste:  python3 test.py 695      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
# @lc code=end
