#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#
# Hard  ·  Intervals
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
#
# Primești o listă de intervale, `intervals[i] = [left, right]` (capetele sunt incluse), și un
# array de interogări, `queries`. Mărimea unui interval e numărul de întregi pe care îi conține:
# `right − left + 1`.
#
# Răspunsul la interogarea `queries[j]` e mărimea celui mai mic interval care o conține (`left ≤
# queries[j] ≤ right`) sau −1 dacă niciun interval n-o conține. Returnează un array cu
# răspunsurile, în ordinea interogărilor.
#
# Exemplul 1
#   Input:  intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
#   Output: [3,3,1,4]
#
# Exemplul 2
#   Input:  intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
#   Output: [2,-1,4,6]
#
# Constrângeri:
#   - `1 ≤ len(intervals) ≤ 10⁵`
#   - `1 ≤ len(queries) ≤ 10⁵`
#   - `len(intervals[i]) == 2`
#   - `1 ≤ left ≤ right ≤ 10⁷`
#   - `1 ≤ queries[j] ≤ 10⁷`
#
# Teste:  python3 test.py 1851      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
# @lc code=end
