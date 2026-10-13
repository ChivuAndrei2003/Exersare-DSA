#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# Medium  ·  Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
#
# Primești o listă de intervale, `intervals[i] = [start, end]`. Returnează numărul minim de
# intervale pe care trebuie să le elimini ca restul să nu se suprapună.
#
# Intervalele care doar se ating într-un punct nu se suprapun: `[1, 2]` și `[2, 3]` pot rămâne
# amândouă.
#
# Exemplul 1
#   Input:  intervals = [[1,2],[2,3],[3,4],[1,3]]
#   Output: 1
#
# Exemplul 2
#   Input:  intervals = [[1,2],[1,2],[1,2]]
#   Output: 2
#
# Exemplul 3
#   Input:  intervals = [[1,2],[2,3]]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(intervals) ≤ 10⁵`
#   - `len(intervals[i]) == 2`
#   - `-5 · 10⁴ ≤ start < end ≤ 5 · 10⁴`
#
# Teste:  python3 test.py 435      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
# @lc code=end
