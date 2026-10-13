#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# Easy  ·  Binary Search
# https://leetcode.com/problems/search-insert-position/
#
# Primești un array sortat de întregi distincți, `nums`, și o valoare `target`. Returnează indexul
# lui `target` dacă există; altfel, indexul la care ar trebui inserat ca array-ul să rămână
# sortat.
#
# Algoritmul trebuie să ruleze în O(log n).
#
# Exemplul 1
#   Input:  nums = [1,3,5,6], target = 5
#   Output: 2
#
# Exemplul 2
#   Input:  nums = [1,3,5,6], target = 2
#   Output: 1
#
# Exemplul 3
#   Input:  nums = [1,3,5,6], target = 7
#   Output: 4
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁴`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#   - `nums` conține valori distincte, sortate crescător
#   - `-10⁴ ≤ target ≤ 10⁴`
#
# Teste:  python3 test.py 35      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
# @lc code=end
