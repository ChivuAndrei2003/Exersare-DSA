#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/decode-ways/
#
# Un mesaj format din litere mari a fost codificat în cifre după regula `"A" → "1"`, `"B" → "2"`,
# …, `"Z" → "26"`.
#
# La decodificare, cifrele trebuie grupate și transformate înapoi în litere, lucru care se poate
# face uneori în mai multe feluri: `"11106"` poate fi `"AAJF"` (1, 1, 10, 6) sau `"KJF"` (11, 10,
# 6). Gruparea (1, 11, 06) nu e validă, pentru că `"06"` nu e un cod (doar `"6"` este).
#
# Primești un string `s` format doar din cifre. Returnează numărul de moduri în care poate fi
# decodat sau 0 dacă nu poate fi decodat deloc. Răspunsul încape pe 32 de biți.
#
# Exemplul 1
#   Input:  s = "12"
#   Output: 2
#
# Exemplul 2
#   Input:  s = "226"
#   Output: 3
#
# Exemplul 3
#   Input:  s = "06"
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 100`
#   - `s` conține doar cifre și poate începe cu zerouri
#
# Teste:  python3 test.py 91      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        
# @lc code=end
