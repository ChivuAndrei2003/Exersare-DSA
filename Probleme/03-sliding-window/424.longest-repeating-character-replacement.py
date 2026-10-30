#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# Medium  ·  Sliding Window
# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# Primești un string `s` și un întreg `k`. Poți alege orice caracter din `s` și îl poți schimba cu
# orice altă literă mare a alfabetului englez; ai voie să faci asta de cel mult `k` ori.
#
# Returnează lungimea celui mai lung substring format dintr-o singură literă repetată pe care îl
# poți obține după aceste operații.
#
# Exemplul 1
#   Input:  s = "ABAB", k = 2
#   Output: 4
#
# Exemplul 2
#   Input:  s = "AABABBA", k = 1
#   Output: 4
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 10⁵`
#   - `s` conține doar litere mari ale alfabetului englez
#   - `0 ≤ k ≤ len(s)`
#
# Teste:  python3 test.py 424      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxfreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfreq = max(maxfreq, count[s[r]])

            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


# @lc code=end
