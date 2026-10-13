#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/minimum-path-sum/
#
# Primești o grilă `grid` de m × n cu numere nenegative. Găsește un drum din colțul stânga-sus
# până în colțul dreapta-jos care minimizează suma numerelor de pe el și returnează acea sumă.
#
# La fiecare pas te poți mișca doar în jos sau la dreapta.
#
# Exemplul 1
#   Input:  grid = [[1,3,1],[1,5,1],[4,2,1]]
#   Output: 7
#
# Exemplul 2
#   Input:  grid = [[1,2,3],[4,5,6]]
#   Output: 12
#
# Constrângeri:
#   - `m == len(grid)`, `n == len(grid[i])`
#   - `1 ≤ m, n ≤ 200`
#   - `0 ≤ grid[i][j] ≤ 200`
#
# Teste:  python3 test.py 64      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
# @lc code=end
