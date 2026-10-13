#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# Easy  ·  Bit Manipulation
# https://leetcode.com/problems/number-of-1-bits/
#
# Primești un întreg nenegativ `n`. Returnează numărul de biți de 1 din reprezentarea lui binară
# (numit și greutatea Hamming).
#
# Follow-up: dacă funcția e apelată de foarte multe ori, cum ai optimiza-o?
#
# Exemplul 1
#   Input:  n = 11
#   Output: 3
#
# Exemplul 2
#   Input:  n = 128
#   Output: 1
#
# Exemplul 3
#   Input:  n = 2147483645
#   Output: 30
#
# Constrângeri:
#   - `0 ≤ n ≤ 2³² − 1` (pe LeetCode: `1 ≤ n ≤ 2³¹ − 1`)
#
# Teste:  python3 test.py 191      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        
# @lc code=end
