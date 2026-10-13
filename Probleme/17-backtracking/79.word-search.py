#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/word-search/
#
# Primești o grilă de caractere `board`, de m × n, și un string `word`. Returnează `True` dacă
# `word` poate fi găsit pe grilă.
#
# Cuvântul se formează din litere aflate în celule adiacente succesive (vecine pe orizontală sau
# pe verticală). Aceeași celulă nu poate fi folosită de două ori.
#
# Follow-up: poți tăia din căutare (pruning) ca soluția să fie mai rapidă pe table mai mari?
#
# Exemplul 1
#   Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#   Output: true
#
# Exemplul 2
#   Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#   Output: true
#
# Exemplul 3
#   Input:  board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#   Output: false
#
# Constrângeri:
#   - `m == len(board)`, `n == len(board[i])`
#   - `1 ≤ m, n ≤ 6`
#   - `1 ≤ len(word) ≤ 15`
#   - `board` și `word` conțin doar litere mici și mari ale alfabetului englez
#
# Teste:  python3 test.py 79      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
# @lc code=end
