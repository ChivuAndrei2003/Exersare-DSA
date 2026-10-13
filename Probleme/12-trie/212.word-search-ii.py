#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# Hard  ·  Trie
# https://leetcode.com/problems/word-search-ii/
#
# Primești o grilă de litere `board`, de m × n, și o listă de cuvinte, `words`. Returnează toate
# cuvintele din listă care pot fi găsite pe grilă.
#
# Un cuvânt se formează din litere aflate în celule adiacente succesive (vecine pe orizontală sau
# pe verticală). Aceeași celulă nu poate fi folosită de două ori în același cuvânt.
#
# Exemplul 1
#   Input:
#     board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#     words = ["oath","pea","eat","rain"]
#   Output: ["eat","oath"]
#
# Exemplul 2
#   Input:  board = [["a","b"],["c","d"]], words = ["abcb"]
#   Output: []
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `m == len(board)`, `n == len(board[i])`
#   - `1 ≤ m, n ≤ 12`
#   - `board[i][j]` e o literă mică a alfabetului englez
#   - `1 ≤ len(words) ≤ 3 · 10⁴`
#   - `1 ≤ len(words[i]) ≤ 10`
#   - `words[i]` conține doar litere mici ale alfabetului englez
#   - Toate cuvintele din `words` sunt distincte
#
# Teste:  python3 test.py 212      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
# @lc code=end
