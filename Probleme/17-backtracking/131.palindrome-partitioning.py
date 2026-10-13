#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/palindrome-partitioning/
#
# Primești un string `s`. Împarte-l în bucăți astfel încât fiecare bucată să fie un palindrom și
# returnează toate împărțirile posibile.
#
# Exemplul 1
#   Input:  s = "aab"
#   Output: [["a","a","b"],["aa","b"]]
#
# Exemplul 2
#   Input:  s = "a"
#   Output: [["a"]]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 16`
#   - `s` conține doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 131      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
# @lc code=end
