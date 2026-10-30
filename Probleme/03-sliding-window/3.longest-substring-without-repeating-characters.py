#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# Medium  ·  Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Primești un string `s`. Returnează lungimea celui mai lung substring (secvență contiguă de
# caractere) în care niciun caracter nu se repetă.
#
# Exemplul 1
#   Input:  s = "abcabcbb"
#   Output: 3
#
# Exemplul 2
#   Input:  s = "bbbbb"
#   Output: 1
#
# Exemplul 3
#   Input:  s = "pwwkew"
#   Output: 3
#
# Constrângeri:
#   - `0 ≤ len(s) ≤ 10⁵`
#   - `s` conține litere ale alfabetului englez, cifre, simboluri și spații
#
# Teste:  python3 test.py 3      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = best = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            best = max(best, r - l + 1)
        return best


# @lc code=end
