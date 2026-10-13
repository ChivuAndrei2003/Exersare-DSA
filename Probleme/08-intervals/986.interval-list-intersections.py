#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# Medium  ·  Intervals
# https://leetcode.com/problems/interval-list-intersections/
#
# Primești două liste de intervale închise, `firstList` și `secondList`. În fiecare listă
# intervalele sunt disjuncte două câte două și sortate crescător.
#
# Returnează intersecția celor două liste: toate intervalele în care un interval din prima listă
# se suprapune cu unul din a doua. Intersecția a două intervale închise e fie vidă, fie tot un
# interval închis — `[1, 3]` ∩ `[2, 4]` = `[2, 3]` — și poate fi chiar un singur punct, ca `[5,
# 5]`.
#
# Exemplul 1
#   Input:
#     firstList = [[0,2],[5,10],[13,23],[24,25]]
#     secondList = [[1,5],[8,12],[15,24],[25,26]]
#   Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
# Exemplul 2
#   Input:  firstList = [[1,3],[5,9]], secondList = []
#   Output: []
#
# Constrângeri:
#   - `0 ≤ len(firstList), len(secondList) ≤ 1000`
#   - `len(firstList) + len(secondList) ≥ 1`
#   - `0 ≤ start < end ≤ 10⁹` pentru fiecare interval
#   - În fiecare listă, un interval se termină înainte să înceapă următorul
#
# Teste:  python3 test.py 986      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
# @lc code=end
