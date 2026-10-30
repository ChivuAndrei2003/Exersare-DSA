#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# Medium  ·  Sliding Window
# https://leetcode.com/problems/minimum-size-subarray-sum/
#
# Primești un array de întregi pozitivi, `nums`, și un întreg pozitiv `target`. Returnează
# lungimea minimă a unui subarray (elemente consecutive) cu suma mai mare sau egală cu `target`.
# Dacă nu există un astfel de subarray, returnează 0.
#
# Follow-up: după soluția O(n), încearcă și una în O(n log n).
#
# Exemplul 1
#   Input:  target = 7, nums = [2,3,1,2,4,3]
#   Output: 2
#
# Exemplul 2
#   Input:  target = 4, nums = [1,4,4]
#   Output: 1
#
# Exemplul 3
#   Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ target ≤ 10⁹`
#   - `1 ≤ len(nums) ≤ 10⁵`
#   - `1 ≤ nums[i] ≤ 10⁴`
#
# Teste:  python3 test.py 209      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        best = float("inf")

        for r, x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if best == float("inf") else best  # type: ignore


# @lc code=end
