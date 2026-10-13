#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/subsets-ii/
#
# Primești un array de întregi `nums` care poate conține duplicate. Returnează toate submulțimile
# posibile.
#
# Rezultatul nu trebuie să conțină submulțimi duplicate (aceleași valori, indiferent de ordine).
# Ordinea nu contează.
#
# Exemplul 1
#   Input:  nums = [1,2,2]
#   Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
# Exemplul 2
#   Input:  nums = [0]
#   Output: [[],[0]]
#
# Notă: Ordinea nu contează (nici în listă, nici în interiorul grupurilor).
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10`
#   - `-10 ≤ nums[i] ≤ 10`
#
# Teste:  python3 test.py 90      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
# @lc code=end
