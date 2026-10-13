#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# Medium  ·  Arrays & Hashing
# https://leetcode.com/problems/product-of-array-except-self/
#
# Primești un array de întregi `nums`. Returnează un array `answer` în care `answer[i]` e produsul
# tuturor elementelor din `nums`, mai puțin `nums[i]`.
#
# Algoritmul trebuie să ruleze în O(n) și fără operația de împărțire.
#
# Follow-up: rezolvă cu memorie suplimentară O(1) (array-ul rezultat nu se pune la socoteală).
#
# Exemplul 1
#   Input:  nums = [1,2,3,4]
#   Output: [24,12,8,6]
#
# Exemplul 2
#   Input:  nums = [-1,1,0,-3,3]
#   Output: [0,0,9,0,0]
#
# Constrângeri:
#   - `2 ≤ len(nums) ≤ 10⁵`
#   - `-30 ≤ nums[i] ≤ 30`
#   - Orice `answer[i]` încape într-un întreg pe 32 de biți
#
# Teste:  python3 test.py 238      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
# @lc code=end
