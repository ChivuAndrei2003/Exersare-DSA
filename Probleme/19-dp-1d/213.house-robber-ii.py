#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/house-robber-ii/
#
# Aceeași poveste ca la House Robber, dar casele sunt așezate în cerc: prima casă e vecină cu
# ultima. Casa `i` are `nums[i]` bani, iar alarma sună dacă două case alăturate sunt sparte în
# aceeași noapte.
#
# Returnează suma maximă pe care o poți fura fără să declanșezi alarma.
#
# Exemplul 1
#   Input:  nums = [2,3,2]
#   Output: 3
#
# Exemplul 2
#   Input:  nums = [1,2,3,1]
#   Output: 4
#
# Exemplul 3
#   Input:  nums = [1,2,3]
#   Output: 3
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 100`
#   - `0 ≤ nums[i] ≤ 1000`
#
# Teste:  python3 test.py 213      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
# @lc code=end
