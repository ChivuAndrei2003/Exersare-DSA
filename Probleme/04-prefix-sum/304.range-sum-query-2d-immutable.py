#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# Medium  ·  Prefix Sum
# https://leetcode.com/problems/range-sum-query-2d-immutable/
#
# Primești o matrice `matrix` de m × n și trebuie să răspunzi la multe interogări: suma
# elementelor din dreptunghiul cu colțul stânga-sus `(row1, col1)` și colțul dreapta-jos `(row2,
# col2)`, inclusiv marginile.
#
# Implementează clasa `NumMatrix`: constructorul `NumMatrix(matrix)` primește matricea, iar
# `sumRegion(row1, col1, row2, col2)` returnează suma. `sumRegion` trebuie să ruleze în O(1).
#
# Exemplul 1
#   Input:
#     operations = ["NumMatrix","sumRegion","sumRegion","sumRegion"]
#     arguments = [
#       [[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],
#       [2,1,4,3],
#       [1,1,2,2],
#       [1,2,2,4]
#     ]
#   Output: [null,8,11,12]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `m == len(matrix)`, `n == len(matrix[i])`
#   - `1 ≤ m, n ≤ 200`
#   - `-10⁴ ≤ matrix[i][j] ≤ 10⁴`
#   - `0 ≤ row1 ≤ row2 < m`
#   - `0 ≤ col1 ≤ col2 < n`
#   - Cel mult 10⁴ apeluri către `sumRegion`
#
# Teste:  python3 test.py 304      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
# @lc code=end
