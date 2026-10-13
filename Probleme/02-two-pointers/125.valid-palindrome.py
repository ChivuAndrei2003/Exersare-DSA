#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# Easy  ·  Two Pointers
# https://leetcode.com/problems/valid-palindrome/
#
# Un text e palindrom dacă, după ce transformi literele mari în litere mici și elimini tot ce nu e
# literă sau cifră, se citește la fel de la stânga la dreapta și de la dreapta la stânga.
#
# Primești un string `s`. Returnează `True` dacă e palindrom în sensul de mai sus și `False`
# altfel. Un string care rămâne gol după curățare e palindrom.
#
# Exemplul 1
#   Input:  s = "A man, a plan, a canal: Panama"
#   Output: true
#
# Exemplul 2
#   Input:  s = "race a car"
#   Output: false
#
# Exemplul 3
#   Input:  s = " "
#   Output: true
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 2 · 10⁵`
#   - `s` conține doar caractere ASCII printabile
#
# Teste:  python3 test.py 125      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
# @lc code=end
