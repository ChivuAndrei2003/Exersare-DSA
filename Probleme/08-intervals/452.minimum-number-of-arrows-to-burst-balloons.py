#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
# Medium  ·  Intervals
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#
# Pe un perete (planul XY) sunt lipite baloane sferice. Balonul `i` e descris prin `points[i] =
# [x_start, x_end]`: diametrul lui orizontal se întinde între aceste coordonate. Înălțimea la care
# se află nu contează.
#
# Săgețile se trag vertical în sus, din orice punct de pe axa x. O săgeată trasă din `x` sparge
# toate baloanele cu `x_start ≤ x ≤ x_end` și își continuă drumul la nesfârșit. Poți trage oricâte
# săgeți.
#
# Returnează numărul minim de săgeți cu care spargi toate baloanele.
#
# Exemplul 1
#   Input:  points = [[10,16],[2,8],[1,6],[7,12]]
#   Output: 2
#
# Exemplul 2
#   Input:  points = [[1,2],[3,4],[5,6],[7,8]]
#   Output: 4
#
# Exemplul 3
#   Input:  points = [[1,2],[2,3],[3,4],[4,5]]
#   Output: 2
#
# Constrângeri:
#   - `1 ≤ len(points) ≤ 10⁵`
#   - `len(points[i]) == 2`
#   - `-2³¹ ≤ x_start < x_end ≤ 2³¹ − 1`
#
# Teste:  python3 test.py 452      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
# @lc code=end
