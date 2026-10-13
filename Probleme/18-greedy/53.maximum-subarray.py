#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# Medium  ·  Greedy
# https://leetcode.com/problems/maximum-subarray/
#
# Primești un array de întregi `nums`. Găsește subarray-ul (contiguu, cu cel puțin un element) cu
# suma maximă și returnează suma lui.
#
# Follow-up: după soluția O(n), încearcă una cu divide et impera.
#
# Exemplul 1
#   Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6
#
# Exemplul 2
#   Input:  nums = [1]
#   Output: 1
#
# Exemplul 3
#   Input:  nums = [5,4,-1,7,8]
#   Output: 23
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁵`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#
# Teste:  python3 test.py 53      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
# @lc code=end
