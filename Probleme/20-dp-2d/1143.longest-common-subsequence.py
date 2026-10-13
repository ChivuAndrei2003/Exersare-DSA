#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/longest-common-subsequence/
#
# Primești două stringuri, `text1` și `text2`. Returnează lungimea celui mai lung subșir comun al
# lor sau 0 dacă nu au niciunul.
#
# Un subșir al unui string se obține ștergând unele caractere (eventual niciunul), fără a schimba
# ordinea celor rămase: `"ace"` e subșir al lui `"abcde"`. Un subșir comun e subșir al ambelor
# stringuri.
#
# Exemplul 1
#   Input:  text1 = "abcde", text2 = "ace"
#   Output: 3
#
# Exemplul 2
#   Input:  text1 = "abc", text2 = "abc"
#   Output: 3
#
# Exemplul 3
#   Input:  text1 = "abc", text2 = "def"
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(text1), len(text2) ≤ 1000`
#   - `text1` și `text2` conțin doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 1143      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
# @lc code=end
