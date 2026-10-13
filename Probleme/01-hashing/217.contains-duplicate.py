#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# Easy  ·  Arrays & Hashing
# https://leetcode.com/problems/contains-duplicate/
#
# Primești un array de întregi `nums`. Returnează `True` dacă vreo valoare apare de cel puțin două
# ori și `False` dacă toate elementele sunt distincte.
#
# Exemplul 1
#   Input:  nums = [1,2,3,1]
#   Output: true
#
# Exemplul 2
#   Input:  nums = [1,2,3,4]
#   Output: false
#
# Exemplul 3
#   Input:  nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁵`
#   - `-10⁹ ≤ nums[i] ≤ 10⁹`
#
# Teste:  python3 test.py 217      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
# @lc code=end
