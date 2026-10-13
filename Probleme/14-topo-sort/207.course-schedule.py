#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# Medium  ·  Topological Sort
# https://leetcode.com/problems/course-schedule/
#
# Ai de urmat `numCourses` cursuri, numerotate de la 0 la `numCourses − 1`. Primești
# `prerequisites`, unde `prerequisites[i] = [a, b]` înseamnă că trebuie să termini cursul `b`
# înainte de cursul `a`.
#
# Returnează `True` dacă poți termina toate cursurile și `False` altfel.
#
# Exemplul 1
#   Input:  numCourses = 2, prerequisites = [[1,0]]
#   Output: true
#
# Exemplul 2
#   Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
#   Output: false
#
# Constrângeri:
#   - `1 ≤ numCourses ≤ 2000`
#   - `0 ≤ len(prerequisites) ≤ 5000`
#   - `len(prerequisites[i]) == 2`
#   - `0 ≤ a, b < numCourses`
#   - Toate perechile din `prerequisites` sunt distincte
#
# Teste:  python3 test.py 207      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
# @lc code=end
