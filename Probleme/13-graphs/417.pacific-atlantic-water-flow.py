#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/pacific-atlantic-water-flow/
#
# O insulă dreptunghiulară de m × n se învecinează cu două oceane: Pacificul atinge marginea de
# sus și pe cea din stânga, iar Atlanticul atinge marginea de jos și pe cea din dreapta. Insula e
# împărțită în celule pătrate, iar `heights[r][c]` e înălțimea celulei `(r, c)` față de nivelul
# mării.
#
# Când plouă, apa curge dintr-o celulă în celulele vecine (nord, sud, est, vest) cu înălțimea mai
# mică sau egală. Din celulele de pe margine apa curge în oceanul alăturat.
#
# Returnează lista coordonatelor `[r, c]` ale celulelor din care apa de ploaie poate ajunge în
# ambele oceane.
#
# Exemplul 1
#   Input:  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#   Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
# Exemplul 2
#   Input:  heights = [[1]]
#   Output: [[0,0]]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `m == len(heights)`, `n == len(heights[r])`
#   - `1 ≤ m, n ≤ 200`
#   - `0 ≤ heights[r][c] ≤ 10⁵`
#
# Teste:  python3 test.py 417      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
# @lc code=end
