#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/surrounded-regions/
#
# Primești o matrice `board` de m × n cu literele `"X"` și `"O"`. O regiune e un grup de celule
# `"O"` legate pe orizontală sau pe verticală. O regiune e înconjurată dacă nicio celulă a ei nu
# se află pe marginea tablei, deci e închisă din toate părțile de `"X"`.
#
# Capturează toate regiunile înconjurate: înlocuiește pe loc fiecare `"O"` din ele cu `"X"`.
# Funcția nu returnează nimic; modifică `board`.
#
# Exemplul 1
#   Input:  board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#   Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Exemplul 2
#   Input:  board = [["X"]]
#   Output: [["X"]]
#
# Notă: Funcția modifică inputul pe loc; se verifică inputul după apel.
#
# Constrângeri:
#   - `m == len(board)`, `n == len(board[i])`
#   - `1 ≤ m, n ≤ 200`
#   - `board[i][j]` e `"X"` sau `"O"`
#
# Teste:  python3 test.py 130      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
# @lc code=end
