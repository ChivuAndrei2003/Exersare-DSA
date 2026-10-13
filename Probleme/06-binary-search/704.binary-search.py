#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# Easy  ·  Binary Search
# https://leetcode.com/problems/binary-search/
#
# Primești un array de întregi `nums`, sortat crescător, și un întreg `target`. Dacă `target` se
# află în `nums`, returnează indexul lui; altfel returnează −1.
#
# Algoritmul trebuie să ruleze în O(log n).
#
# Exemplul 1
#   Input:  nums = [-1,0,3,5,9,12], target = 9
#   Output: 4
#
# Exemplul 2
#   Input:  nums = [-1,0,3,5,9,12], target = 2
#   Output: -1
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁴`
#   - `-10⁴ < nums[i], target < 10⁴`
#   - Toate valorile din `nums` sunt distincte
#   - `nums` e sortat crescător
#
# Teste:  python3 test.py 704      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
# @lc code=end
