#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# Medium  ·  Shortest Path (Dijkstra)
# https://leetcode.com/problems/network-delay-time/
#
# Ai o rețea cu `n` noduri, numerotate de la 1 la `n`. Primești `times`, timpii de propagare pe
# muchii orientate: `times[i] = [u, v, w]` înseamnă că un semnal ajunge de la `u` la `v` în `w`
# unități de timp.
#
# Trimiți un semnal din nodul `k`. Returnează timpul minim după care toate cele `n` noduri au
# primit semnalul sau −1 dacă nu pot ajunge toate să-l primească.
#
# Exemplul 1
#   Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#   Output: 2
#
# Exemplul 2
#   Input:  times = [[1,2,1]], n = 2, k = 1
#   Output: 1
#
# Exemplul 3
#   Input:  times = [[1,2,1]], n = 2, k = 2
#   Output: -1
#
# Constrângeri:
#   - `1 ≤ k ≤ n ≤ 100`
#   - `0 ≤ len(times) ≤ 6000` (pe LeetCode, cel puțin o muchie)
#   - `len(times[i]) == 3`
#   - `1 ≤ u, v ≤ n`
#   - `u ≠ v`
#   - `0 ≤ w ≤ 100`
#   - Toate perechile `(u, v)` sunt distincte (fără muchii multiple)
#
# Teste:  python3 test.py 743      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
# @lc code=end
