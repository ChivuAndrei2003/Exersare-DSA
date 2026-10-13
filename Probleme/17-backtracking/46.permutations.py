#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/permutations/
#
# Primești un array `nums` de întregi distincți. Returnează toate permutările posibile, în orice
# ordine.
#
# Exemplul 1
#   Input:  nums = [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Exemplul 2
#   Input:  nums = [0,1]
#   Output: [[0,1],[1,0]]
#
# Exemplul 3
#   Input:  nums = [1]
#   Output: [[1]]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 6`
#   - `-10 ≤ nums[i] ≤ 10`
#   - Toate valorile din `nums` sunt distincte
#
# Teste:  python3 test.py 46      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
# @lc code=end
