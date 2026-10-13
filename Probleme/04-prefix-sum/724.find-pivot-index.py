#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
# Easy  ·  Prefix Sum
# https://leetcode.com/problems/find-pivot-index/
#
# Primești un array de întregi `nums`. Indexul pivot e indexul la care suma tuturor elementelor
# strict din stânga lui e egală cu suma tuturor elementelor strict din dreapta lui.
#
# La marginea din stânga suma din stânga e 0 (nu există elemente acolo); la fel pentru marginea
# din dreapta. Returnează cel mai din stânga index pivot sau −1 dacă nu există niciunul.
#
# Exemplul 1
#   Input:  nums = [1,7,3,6,5,6]
#   Output: 3
#
# Exemplul 2
#   Input:  nums = [1,2,3]
#   Output: -1
#
# Exemplul 3
#   Input:  nums = [2,1,-1]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁴`
#   - `-1000 ≤ nums[i] ≤ 1000`
#
# Teste:  python3 test.py 724      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
# @lc code=end
