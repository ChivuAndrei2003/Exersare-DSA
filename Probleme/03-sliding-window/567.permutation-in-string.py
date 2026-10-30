#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# Medium  ·  Sliding Window
# https://leetcode.com/problems/permutation-in-string/
#
# Primești două stringuri, `s1` și `s2`. Returnează `True` dacă `s2` conține o permutare a lui
# `s1` — adică una dintre permutările lui `s1` apare ca substring în `s2` — și `False` altfel.
#
# Exemplul 1
#   Input:  s1 = "ab", s2 = "eidbaooo"
#   Output: true
#
# Exemplul 2
#   Input:  s1 = "ab", s2 = "eidboaoo"
#   Output: false
#
# Constrângeri:
#   - `1 ≤ len(s1), len(s2) ≤ 10⁴`
#   - `s1` și `s2` conțin doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 567      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


# @lc code=end
