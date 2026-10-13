#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# Easy  ·  Trie
# https://leetcode.com/problems/longest-common-prefix/
#
# Primești un array de stringuri, `strs`. Returnează cel mai lung prefix comun tuturor
# stringurilor. Dacă nu au niciun prefix comun, returnează stringul gol `""`.
#
# Exemplul 1
#   Input:  strs = ["flower","flow","flight"]
#   Output: "fl"
#
# Exemplul 2
#   Input:  strs = ["dog","racecar","car"]
#   Output: ""
#
# Constrângeri:
#   - `1 ≤ len(strs) ≤ 200`
#   - `0 ≤ len(strs[i]) ≤ 200`
#   - `strs[i]`, dacă nu e gol, conține doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 14      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
# @lc code=end
