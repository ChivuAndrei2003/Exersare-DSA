#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# Medium  ·  Topological Sort
# https://leetcode.com/problems/course-schedule-ii/
#
# Ai de urmat `numCourses` cursuri, numerotate de la 0 la `numCourses − 1`. Primești
# `prerequisites`, unde `prerequisites[i] = [a, b]` înseamnă că trebuie să termini cursul `b`
# înainte de cursul `a`.
#
# Returnează o ordine în care poți urma toate cursurile. Dacă sunt mai multe ordini valide,
# returnează oricare; dacă e imposibil să le termini pe toate, returnează un array gol.
#
# Exemplul 1
#   Input:  numCourses = 2, prerequisites = [[1,0]]
#   Output: [0,1]
#
# Exemplul 2
#   Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#   Output: [0,2,1,3]
#
# Exemplul 3
#   Input:  numCourses = 1, prerequisites = []
#   Output: [0]
#
# Notă: Orice ordine validă e acceptată.
#
# Constrângeri:
#   - `1 ≤ numCourses ≤ 2000`
#   - `0 ≤ len(prerequisites) ≤ numCourses · (numCourses − 1)`
#   - `len(prerequisites[i]) == 2`
#   - `0 ≤ a, b < numCourses`
#   - `a ≠ b`
#   - Toate perechile `[a, b]` sunt distincte
#
# Teste:  python3 test.py 210      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
# @lc code=end
