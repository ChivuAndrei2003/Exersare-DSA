#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# Easy  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/climbing-stairs/
#
# Urci o scară cu `n` trepte. La fiecare pas poți urca 1 sau 2 trepte.
#
# În câte moduri distincte poți ajunge sus?
#
# Exemplul 1
#   Input:  n = 2
#   Output: 2
#
# Exemplul 2
#   Input:  n = 3
#   Output: 3
#
# Constrângeri:
#   - `1 ≤ n ≤ 45`
#
# Teste:  python3 test.py 70      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        
# @lc code=end
