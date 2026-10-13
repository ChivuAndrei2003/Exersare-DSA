#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# Medium  ·  Heap / Top K
# https://leetcode.com/problems/k-closest-points-to-origin/
#
# Primești un array de puncte din plan, `points[i] = [x, y]`, și un întreg `k`. Returnează cele
# mai apropiate `k` puncte de origine, `(0, 0)`.
#
# Distanța e cea euclidiană: `√(x² + y²)`. Răspunsul poate fi dat în orice ordine și e unic (mai
# puțin ordinea).
#
# Exemplul 1
#   Input:  points = [[1,3],[-2,2]], k = 1
#   Output: [[-2,2]]
#
# Exemplul 2
#   Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
#   Output: [[3,3],[-2,4]]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ k ≤ len(points) ≤ 10⁴`
#   - `-10⁴ ≤ x, y ≤ 10⁴`
#
# Teste:  python3 test.py 973      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
# @lc code=end
