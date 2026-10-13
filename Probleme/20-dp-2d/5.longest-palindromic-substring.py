#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Primești un string `s`. Returnează cel mai lung substring al lui `s` care e palindrom (se
# citește la fel în ambele sensuri).
#
# Exemplul 1
#   Input:  s = "babad"
#   Output: "bab"
#
# Exemplul 2
#   Input:  s = "cbbd"
#   Output: "bb"
#
# Notă: Dacă sunt mai multe răspunsuri corecte, oricare e acceptat.
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 1000`
#   - `s` conține doar cifre și litere ale alfabetului englez
#
# Teste:  python3 test.py 5      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
# @lc code=end
