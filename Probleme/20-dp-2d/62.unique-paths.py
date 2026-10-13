#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/unique-paths/
#
# Un robot se află în colțul stânga-sus al unei grile de `m × n` și vrea să ajungă în colțul
# dreapta-jos. La fiecare pas se poate mișca doar în jos sau la dreapta.
#
# Primești `m` și `n`. Returnează numărul de drumuri distincte pe care le poate urma. Răspunsul e
# cel mult 2 · 10⁹.
#
# Exemplul 1
#   Input:  m = 3, n = 7
#   Output: 28
#
# Exemplul 2
#   Input:  m = 3, n = 2
#   Output: 3
#
# Constrângeri:
#   - `1 ≤ m, n ≤ 100`
#
# Teste:  python3 test.py 62      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
# @lc code=end
