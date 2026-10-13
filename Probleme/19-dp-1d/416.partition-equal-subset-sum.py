#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/partition-equal-subset-sum/
#
# Primești un array de întregi `nums`. Returnează `True` dacă îl poți împărți în două submulțimi
# cu sume egale și `False` altfel.
#
# Exemplul 1
#   Input:  nums = [1,5,11,5]
#   Output: true
#
# Exemplul 2
#   Input:  nums = [1,2,3,5]
#   Output: false
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 200`
#   - `1 ≤ nums[i] ≤ 100`
#
# Teste:  python3 test.py 416      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
# @lc code=end
