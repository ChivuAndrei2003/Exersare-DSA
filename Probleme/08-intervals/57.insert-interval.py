#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# Medium  ·  Intervals
# https://leetcode.com/problems/insert-interval/
#
# Primești `intervals`, o listă de intervale care nu se suprapun, sortată crescător după start
# (`intervals[i] = [start, end]`), și un interval nou, `newInterval`.
#
# Inserează `newInterval` astfel încât lista să rămână sortată după start și fără suprapuneri,
# unind intervalele unde e nevoie. Returnează lista rezultată; nu e obligatoriu s-o modifici pe
# cea primită.
#
# Exemplul 1
#   Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
#   Output: [[1,5],[6,9]]
#
# Exemplul 2
#   Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#   Output: [[1,2],[3,10],[12,16]]
#
# Constrângeri:
#   - `0 ≤ len(intervals) ≤ 10⁴`
#   - `len(intervals[i]) == 2` și `len(newInterval) == 2`
#   - `0 ≤ start ≤ end ≤ 10⁵` pentru toate intervalele, inclusiv `newInterval`
#   - `intervals` e sortată crescător după start
#
# Teste:  python3 test.py 57      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
# @lc code=end
