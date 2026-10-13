#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/subsets/
#
# Primești un array `nums` de întregi distincți. Returnează toate submulțimile posibile (mulțimea
# părților), inclusiv mulțimea vidă și `nums` întreg.
#
# Rezultatul nu trebuie să conțină submulțimi duplicate. Ordinea nu contează.
#
# Exemplul 1
#   Input:  nums = [1,2,3]
#   Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
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
#   - Toate numerele din `nums` sunt distincte
#
# Teste:  python3 test.py 78      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
# @lc code=end
