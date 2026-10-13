#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
# Hard  ·  Shortest Path (Dijkstra)
# https://leetcode.com/problems/swim-in-rising-water/
#
# Primești o matrice `grid` de n × n, unde `grid[i][j]` e altitudinea punctului `(i, j)`. Începe
# să plouă: la momentul `t`, nivelul apei e `t` peste tot.
#
# Poți înota dintr-o celulă în una vecină pe cele 4 direcții doar dacă altitudinea ambelor celule
# e cel mult `t`. Înotul în sine nu durează: într-un moment poți parcurge orice distanță, cât timp
# rămâi în grilă.
#
# Pornești din colțul stânga-sus, `(0, 0)`. Returnează cel mai mic moment `t` la care poți ajunge
# în colțul dreapta-jos, `(n − 1, n − 1)`.
#
# Exemplul 1
#   Input:  grid = [[0,2],[1,3]]
#   Output: 3
#
# Exemplul 2
#   Input:  grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
#   Output: 16
#
# Constrângeri:
#   - `n == len(grid) == len(grid[i])`
#   - `1 ≤ n ≤ 50`
#   - `0 ≤ grid[i][j] < n²`
#   - Toate valorile din `grid` sunt distincte
#
# Teste:  python3 test.py 778      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
# @lc code=end
