#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#
# Easy  ·  Bit Manipulation
# https://leetcode.com/problems/reverse-bits/
#
# Primești `n`, un întreg fără semn pe 32 de biți. Inversează ordinea biților lui și returnează
# numărul obținut: bitul cel mai puțin semnificativ devine cel mai semnificativ și invers.
#
# Follow-up: dacă funcția e apelată de foarte multe ori, cum ai optimiza-o?
#
# Exemplul 1
#   Input:  n = 43261596
#   Output: 964176192
#
# Exemplul 2
#   Input:  n = 2147483644
#   Output: 1073741822
#
# Constrângeri:
#   - `0 ≤ n ≤ 2³² − 1` (pe LeetCode: `n` par, `0 ≤ n ≤ 2³¹ − 2`)
#
# Teste:  python3 test.py 190      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        
# @lc code=end
