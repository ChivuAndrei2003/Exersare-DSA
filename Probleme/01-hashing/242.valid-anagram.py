#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# Easy  ·  Arrays & Hashing
# https://leetcode.com/problems/valid-anagram/
#
# Primești două stringuri, `s` și `t`.
# Returnează `True` dacă `t` e o anagramă a lui `s`
# — se obține rearanjând literele lui `s`,
# fiecare folosită exact de câte ori apare — și `False`
# altfel.
#
# Exemplul 1
#   Input:  s = "anagram", t = "nagaram"
#   Output: true
#
# Exemplul 2
#   Input:  s = "rat", t = "car"
#   Output: false
#
# Constrângeri:
#   - `1 ≤ len(s), len(t) ≤ 5 · 10⁴`
#   - `s` și `t` conțin doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 242      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  # pyright: ignore[reportReturnType]
        return sorted(s) == sorted(t)


# @lc code=end
