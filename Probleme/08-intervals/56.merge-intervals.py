#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# Medium  ·  Intervals
# https://leetcode.com/problems/merge-intervals/
#
# Primești o listă de intervale, `intervals[i] = [start, end]`. Unește toate intervalele care se
# suprapun și returnează o listă de intervale disjuncte care acoperă exact aceleași puncte.
#
# Două intervale care doar se ating, ca `[1, 4]` și `[4, 5]`, se consideră suprapuse.
#
# Exemplul 1
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
# Exemplul 2
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#
# Exemplul 3
#   Input:  intervals = [[4,7],[1,4]]
#   Output: [[1,7]]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ len(intervals) ≤ 10⁴`
#   - `len(intervals[i]) == 2`
#   - `0 ≤ start ≤ end ≤ 10⁴`
#
# Teste:  python3 test.py 56      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
# @lc code=end
