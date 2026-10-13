#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# Medium  ·  Prefix Sum
# https://leetcode.com/problems/subarray-sum-equals-k/
#
# Primești un array de întregi `nums` și un întreg `k`. Returnează numărul total de subarray-uri
# (secvențe contigue, nevide) a căror sumă e exact `k`.
#
# Exemplul 1
#   Input:  nums = [1,1,1], k = 2
#   Output: 2
#
# Exemplul 2
#   Input:  nums = [1,2,3], k = 3
#   Output: 2
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 2 · 10⁴`
#   - `-1000 ≤ nums[i] ≤ 1000`
#   - `-10⁷ ≤ k ≤ 10⁷`
#
# Teste:  python3 test.py 560      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
# @lc code=end
