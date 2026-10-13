#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# Hard  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/largest-rectangle-in-histogram/
#
# Primești `heights`, înălțimile barelor unei histograme; fiecare bară are lățimea 1. Returnează
# aria celui mai mare dreptunghi care încape în histogramă.
#
# Exemplul 1
#   Input:  heights = [2,1,5,6,2,3]
#   Output: 10
#
# Exemplul 2
#   Input:  heights = [2,4]
#   Output: 4
#
# Constrângeri:
#   - `1 ≤ len(heights) ≤ 10⁵`
#   - `0 ≤ heights[i] ≤ 10⁴`
#
# Teste:  python3 test.py 84      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
# @lc code=end
