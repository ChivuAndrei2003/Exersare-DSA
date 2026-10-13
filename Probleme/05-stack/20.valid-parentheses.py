#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# Easy  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/valid-parentheses/
#
# Primești un string `s` format doar din caracterele `(`, `)`, `{`, `}`, `[` și `]`. Stabilește
# dacă e valid.
#
# Stringul e valid dacă: fiecare paranteză deschisă e închisă de una de același tip; parantezele
# se închid în ordinea corectă; fiecare paranteză închisă are o pereche deschisă de același tip.
#
# Exemplul 1
#   Input:  s = "()"
#   Output: true
#
# Exemplul 2
#   Input:  s = "()[]{}"
#   Output: true
#
# Exemplul 3
#   Input:  s = "(]"
#   Output: false
#
# Exemplul 4
#   Input:  s = "([])"
#   Output: true
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 10⁴`
#   - `s` conține doar caracterele `()[]{}`
#
# Teste:  python3 test.py 20      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
# @lc code=end
