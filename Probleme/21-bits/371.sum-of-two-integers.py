#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# Medium  ·  Bit Manipulation
# https://leetcode.com/problems/sum-of-two-integers/
#
# Primești doi întregi, `a` și `b`. Returnează suma lor fără să folosești operatorii `+` și `-`.
#
# Exemplul 1
#   Input:  a = 1, b = 2
#   Output: 3
#
# Exemplul 2
#   Input:  a = 2, b = 3
#   Output: 5
#
# Constrângeri:
#   - `-1000 ≤ a, b ≤ 1000`
#
# Teste:  python3 test.py 371      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
# @lc code=end
