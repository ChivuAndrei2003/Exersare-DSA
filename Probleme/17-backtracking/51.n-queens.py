#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# Hard  ·  Backtracking
# https://leetcode.com/problems/n-queens/
#
# Problema celor n regine: așază `n` regine pe o tablă de șah de n × n astfel încât oricare două
# să nu se atace — să nu fie pe același rând, pe aceeași coloană sau pe aceeași diagonală.
#
# Primești un întreg `n`. Returnează toate soluțiile distincte, în orice ordine. Fiecare soluție e
# o configurație a tablei: o listă de `n` stringuri de lungime `n`, în care `"Q"` e o regină și
# `"."` o celulă goală.
#
# Exemplul 1
#   Input:  n = 4
#   Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#
# Exemplul 2
#   Input:  n = 1
#   Output: [["Q"]]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ n ≤ 9`
#
# Teste:  python3 test.py 51      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
# @lc code=end
