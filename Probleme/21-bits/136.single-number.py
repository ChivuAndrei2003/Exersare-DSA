#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# Easy  ·  Bit Manipulation
# https://leetcode.com/problems/single-number/
#
# Primești un array nevid de întregi, `nums`, în care fiecare element apare de două ori, cu
# excepția unuia, care apare o singură dată. Găsește-l.
#
# Soluția trebuie să ruleze în timp liniar și cu memorie suplimentară constantă.
#
# Exemplul 1
#   Input:  nums = [2,2,1]
#   Output: 1
#
# Exemplul 2
#   Input:  nums = [4,1,2,1,2]
#   Output: 4
#
# Exemplul 3
#   Input:  nums = [1]
#   Output: 1
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 3 · 10⁴`
#   - `-3 · 10⁴ ≤ nums[i] ≤ 3 · 10⁴`
#   - Fiecare element apare de două ori, cu excepția unuia care apare o singură dată
#
# Teste:  python3 test.py 136      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
# @lc code=end
