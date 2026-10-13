#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/maximum-product-subarray/
#
# Primești un array de întregi `nums`. Găsește subarray-ul (contiguu, nevid) cu produsul maxim și
# returnează produsul lui.
#
# Exemplul 1
#   Input:  nums = [2,3,-2,4]
#   Output: 6
#
# Exemplul 2
#   Input:  nums = [-2,0,-1]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 2 · 10⁴`
#   - `-10 ≤ nums[i] ≤ 10`
#   - Produsul oricărui subarray încape pe 32 de biți
#
# Teste:  python3 test.py 152      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
# @lc code=end
