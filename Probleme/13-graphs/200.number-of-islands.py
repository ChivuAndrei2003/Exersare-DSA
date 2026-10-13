#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/number-of-islands/
#
# Primești o grilă `grid` de m × n, în care `"1"` înseamnă uscat și `"0"` înseamnă apă. Returnează
# numărul de insule.
#
# O insulă e formată din celule de uscat legate pe orizontală sau pe verticală și e înconjurată de
# apă. Marginile grilei se consideră înconjurate de apă.
#
# Exemplul 1
#   Input:
#     grid = [
#       ["1","1","1","1","0"],
#       ["1","1","0","1","0"],
#       ["1","1","0","0","0"],
#       ["0","0","0","0","0"]
#     ]
#   Output: 1
#
# Exemplul 2
#   Input:
#     grid = [
#       ["1","1","0","0","0"],
#       ["1","1","0","0","0"],
#       ["0","0","1","0","0"],
#       ["0","0","0","1","1"]
#     ]
#   Output: 3
#
# Constrângeri:
#   - `m == len(grid)`, `n == len(grid[i])`
#   - `1 ≤ m, n ≤ 300`
#   - `grid[i][j]` e `"0"` sau `"1"`
#
# Teste:  python3 test.py 200      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
# @lc code=end
