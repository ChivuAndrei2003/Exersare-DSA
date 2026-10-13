#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# Medium  ·  Binary Search
# https://leetcode.com/problems/search-a-2d-matrix/
#
# Primești o matrice de întregi `matrix`, de m × n, cu două proprietăți: fiecare rând e sortat
# crescător, iar primul element al fiecărui rând e mai mare decât ultimul element al rândului
# anterior.
#
# Returnează `True` dacă `target` se află în matrice și `False` altfel. Soluția trebuie să ruleze
# în O(log(m · n)).
#
# Exemplul 1
#   Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#   Output: true
#
# Exemplul 2
#   Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#   Output: false
#
# Constrângeri:
#   - `m == len(matrix)`, `n == len(matrix[i])`
#   - `1 ≤ m, n ≤ 100`
#   - `-10⁴ ≤ matrix[i][j], target ≤ 10⁴`
#
# Teste:  python3 test.py 74      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
# @lc code=end
