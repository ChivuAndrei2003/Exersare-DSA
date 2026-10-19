#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# Medium  ·  Arrays & Hashing
# https://leetcode.com/problems/valid-sudoku/
#
# Primești o tablă de Sudoku de 9 × 9, `board`, completată parțial: fiecare celulă e o cifră de la
# `"1"` la `"9"` sau `"."` (celulă goală). Stabilește dacă tabla e validă, uitându-te doar la
# celulele completate.
#
# Tabla e validă dacă nicio cifră nu se repetă pe același rând, pe aceeași coloană sau în același
# pătrat de 3 × 3 (din cele nouă în care se împarte tabla).
#
# O tablă validă nu e neapărat rezolvabilă: nu trebuie să verifici dacă are soluție.
#
# Exemplul 1
#   Input:
#     board = [
#       ["5","3",".",".","7",".",".",".","."],
#       ["6",".",".","1","9","5",".",".","."],
#       [".","9","8",".",".",".",".","6","."],
#       ["8",".",".",".","6",".",".",".","3"],
#       ["4",".",".","8",".","3",".",".","1"],
#       ["7",".",".",".","2",".",".",".","6"],
#       [".","6",".",".",".",".","2","8","."],
#       [".",".",".","4","1","9",".",".","5"],
#       [".",".",".",".","8",".",".","7","9"]
#     ]
#   Output: true
#
# Exemplul 2
#   Input:
#     board = [
#       ["8","3",".",".","7",".",".",".","."],
#       ["6",".",".","1","9","5",".",".","."],
#       [".","9","8",".",".",".",".","6","."],
#       ["8",".",".",".","6",".",".",".","3"],
#       ["4",".",".","8",".","3",".",".","1"],
#       ["7",".",".",".","2",".",".",".","6"],
#       [".","6",".",".",".",".","2","8","."],
#       [".",".",".","4","1","9",".",".","5"],
#       [".",".",".",".","8",".",".","7","9"]
#     ]
#   Output: false
#
# Constrângeri:
#   - `len(board) == 9` și `len(board[i]) == 9`
#   - `board[i][j]` e o cifră `1`–`9` sau `.`
#
# Teste:  python3 test.py 36      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def isValidSudoku(
        self, board: List[List[str]]
    ) -> bool:  # pyright: ignore[reportReturnType]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":  # blank cell is skipped
                    continue

                b = (r // 3) * 3 + c // 3  # index of the 3x3 square

                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)
        return True


# @lc code=end
