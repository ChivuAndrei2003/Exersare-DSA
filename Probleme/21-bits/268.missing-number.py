#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# Easy  ·  Bit Manipulation
# https://leetcode.com/problems/missing-number/
#
# Primești un array `nums` cu `n` numere distincte din intervalul `[0, n]`. Returnează singurul
# număr din interval care lipsește din array.
#
# Follow-up: rezolvă cu memorie suplimentară O(1) și timp O(n).
#
# Exemplul 1
#   Input:  nums = [3,0,1]
#   Output: 2
#
# Exemplul 2
#   Input:  nums = [0,1]
#   Output: 2
#
# Exemplul 3
#   Input:  nums = [9,6,4,2,3,5,7,0,1]
#   Output: 8
#
# Constrângeri:
#   - `n == len(nums)`
#   - `1 ≤ n ≤ 10⁴`
#   - `0 ≤ nums[i] ≤ n`
#   - Toate numerele din `nums` sunt distincte
#
# Teste:  python3 test.py 268      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
# @lc code=end
