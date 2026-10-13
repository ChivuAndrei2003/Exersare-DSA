#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# Medium  ·  Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# Un array de întregi distincți, sortat crescător, a fost eventual rotit în jurul unui index
# necunoscut: `[0, 1, 2, 4, 5, 6, 7]` poate deveni, de exemplu, `[4, 5, 6, 7, 0, 1, 2]`.
#
# Primești array-ul de după rotire, `nums`, și un întreg `target`. Returnează indexul lui `target`
# în `nums` sau −1 dacă nu există. Algoritmul trebuie să ruleze în O(log n).
#
# Exemplul 1
#   Input:  nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
#
# Exemplul 2
#   Input:  nums = [4,5,6,7,0,1,2], target = 3
#   Output: -1
#
# Exemplul 3
#   Input:  nums = [1], target = 0
#   Output: -1
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 5000`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#   - Toate valorile din `nums` sunt distincte
#   - `nums` e un array crescător, eventual rotit
#   - `-10⁴ ≤ target ≤ 10⁴`
#
# Teste:  python3 test.py 33      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
# @lc code=end
