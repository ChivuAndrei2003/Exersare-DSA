#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# Medium  ·  Prefix Sum
# https://leetcode.com/problems/contiguous-array/
#
# Primești un array binar `nums` (doar 0 și 1). Returnează lungimea maximă a unui subarray
# contiguu care conține tot atâția de 0 câți de 1. Dacă nu există niciunul, răspunsul e 0.
#
# Exemplul 1
#   Input:  nums = [0,1]
#   Output: 2
#
# Exemplul 2
#   Input:  nums = [0,1,0]
#   Output: 2
#
# Exemplul 3
#   Input:  nums = [0,1,1,1,1,1,0,0,0]
#   Output: 6
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁵`
#   - `nums[i]` e 0 sau 1
#
# Teste:  python3 test.py 525      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
# @lc code=end
