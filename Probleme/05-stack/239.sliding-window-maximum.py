#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# Hard  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/sliding-window-maximum/
#
# Primești un array de întregi `nums` și o fereastră de mărime `k` care glisează de la capătul din
# stânga la cel din dreapta, câte o poziție pe pas. Prin fereastră vezi doar `k` numere.
#
# Returnează maximul din fiecare poziție a ferestrei, în ordine.
#
# Exemplul 1
#   Input:  nums = [1,3,-1,-3,5,3,6,7], k = 3
#   Output: [3,3,5,5,6,7]
#
# Exemplul 2
#   Input:  nums = [1], k = 1
#   Output: [1]
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁵`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#   - `1 ≤ k ≤ len(nums)`
#
# Teste:  python3 test.py 239      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
# @lc code=end
