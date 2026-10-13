#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# Medium  ·  Greedy
# https://leetcode.com/problems/valid-parenthesis-string/
#
# Primești un string `s` care conține doar trei tipuri de caractere: `(`, `)` și `*`. Returnează
# `True` dacă `s` e valid.
#
# Reguli: orice `(` trebuie să aibă un `)` corespondent, aflat după ea; orice `)` trebuie să aibă
# un `(` corespondent, aflat înaintea ei; iar `*` poate fi tratată ca `(`, ca `)` sau ca string
# gol.
#
# Exemplul 1
#   Input:  s = "()"
#   Output: true
#
# Exemplul 2
#   Input:  s = "(*)"
#   Output: true
#
# Exemplul 3
#   Input:  s = "(*))"
#   Output: true
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 100`
#   - `s[i]` e `(`, `)` sau `*`
#
# Teste:  python3 test.py 678      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        
# @lc code=end
