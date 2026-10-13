#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#
# Medium  ·  Union-Find (DSU)
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#
# Primești un array de puncte din plan, `points[i] = [x, y]`. Costul legării a două puncte, `[x1,
# y1]` și `[x2, y2]`, e distanța Manhattan dintre ele: `|x1 − x2| + |y1 − y2|`.
#
# Returnează costul minim cu care toate punctele ajung conectate. Punctele sunt conectate dacă
# între oricare două există exact un drum simplu.
#
# Exemplul 1
#   Input:  points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
#   Output: 20
#
# Exemplul 2
#   Input:  points = [[3,12],[-2,5],[-4,1]]
#   Output: 18
#
# Constrângeri:
#   - `1 ≤ len(points) ≤ 1000`
#   - `-10⁶ ≤ x, y ≤ 10⁶`
#   - Toate punctele sunt distincte
#
# Teste:  python3 test.py 1584      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
# @lc code=end
