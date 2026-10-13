#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# Medium  ·  Shortest Path (Dijkstra)
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
#
# Există `n` orașe legate prin zboruri. Primești `flights`, unde `flights[i] = [from, to, price]`
# e un zbor într-un singur sens, de la orașul `from` la orașul `to`, cu prețul `price`.
#
# Primești și trei întregi: `src`, `dst` și `k`. Returnează cel mai mic preț al unei călătorii de
# la `src` la `dst` cu **cel mult `k` escale** (deci cel mult `k + 1` zboruri). Dacă nu există o
# astfel de rută, returnează −1.
#
# Exemplul 1
#   Input:
#     n = 4
#     flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
#     src = 0
#     dst = 3
#     k = 1
#   Output: 700
#
# Exemplul 2
#   Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
#   Output: 200
#
# Exemplul 3
#   Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
#   Output: 500
#
# Constrângeri:
#   - `2 ≤ n ≤ 100`
#   - `0 ≤ len(flights) ≤ n · (n − 1) / 2`
#   - `len(flights[i]) == 3`
#   - `0 ≤ from, to < n`
#   - `from ≠ to`
#   - `1 ≤ price ≤ 10⁴`
#   - Nu există mai multe zboruri între aceleași două orașe
#   - `0 ≤ src, dst, k < n`
#   - `src ≠ dst`
#
# Teste:  python3 test.py 787      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
# @lc code=end
