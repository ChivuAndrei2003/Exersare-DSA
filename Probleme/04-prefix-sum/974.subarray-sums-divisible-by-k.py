#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# Medium  ·  Prefix Sum
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
#
# Primești un array de întregi `nums` și un întreg `k`. Returnează numărul de subarray-uri
# contigue și nevide a căror sumă e divizibilă cu `k`.
#
# Exemplul 1
#   Input:  nums = [4,5,0,-2,-3,1], k = 5
#   Output: 7
#
# Exemplul 2
#   Input:  nums = [5], k = 9
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 3 · 10⁴`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#   - `2 ≤ k ≤ 10⁴`
#
# Teste:  python3 test.py 974      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
# @lc code=end
