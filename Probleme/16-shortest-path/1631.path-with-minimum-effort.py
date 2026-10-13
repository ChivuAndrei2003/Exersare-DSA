#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#
# Medium  ·  Shortest Path (Dijkstra)
# https://leetcode.com/problems/path-with-minimum-effort/
#
# Ești un drumeț. Primești `heights`, o hartă de `rows × columns`, unde `heights[row][col]` e
# înălțimea celulei. Pornești din celula stânga-sus, `(0, 0)`, și vrei să ajungi în cea din
# dreapta-jos; te poți mișca sus, jos, la stânga sau la dreapta.
#
# Efortul unui traseu e cea mai mare diferență absolută de înălțime dintre două celule consecutive
# de pe el. Returnează efortul minim cu care poți ajunge la destinație.
#
# Exemplul 1
#   Input:  heights = [[1,2,2],[3,8,2],[5,3,5]]
#   Output: 2
#
# Exemplul 2
#   Input:  heights = [[1,2,3],[3,8,4],[5,3,5]]
#   Output: 1
#
# Exemplul 3
#   Input:  heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
#   Output: 0
#
# Constrângeri:
#   - `rows == len(heights)`, `columns == len(heights[i])`
#   - `1 ≤ rows, columns ≤ 100`
#   - `1 ≤ heights[i][j] ≤ 10⁶`
#
# Teste:  python3 test.py 1631      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
# @lc code=end
