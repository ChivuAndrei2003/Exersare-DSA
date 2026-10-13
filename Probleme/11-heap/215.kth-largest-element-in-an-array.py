#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# Medium  ·  Heap / Top K
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Primești un array de întregi `nums` și un întreg `k`. Returnează al `k`-lea cel mai mare element
# din array.
#
# E vorba de al `k`-lea în ordine sortată descrescător (duplicatele se numără), nu de al `k`-lea
# element distinct. Follow-up: poți rezolva fără să sortezi?
#
# Exemplul 1
#   Input:  nums = [3,2,1,5,6,4], k = 2
#   Output: 5
#
# Exemplul 2
#   Input:  nums = [3,2,3,1,2,4,5,5,6], k = 4
#   Output: 4
#
# Constrângeri:
#   - `1 ≤ k ≤ len(nums) ≤ 10⁵`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#
# Teste:  python3 test.py 215      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
# @lc code=end
