#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/word-break/
#
# Primești un string `s` și un dicționar de cuvinte, `wordDict`. Returnează `True` dacă `s` poate
# fi împărțit într-o secvență de unul sau mai multe cuvinte din dicționar.
#
# Același cuvânt din dicționar poate fi folosit de mai multe ori.
#
# Exemplul 1
#   Input:  s = "leetcode", wordDict = ["leet","code"]
#   Output: true
#
# Exemplul 2
#   Input:  s = "applepenapple", wordDict = ["apple","pen"]
#   Output: true
#
# Exemplul 3
#   Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#   Output: false
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 300`
#   - `1 ≤ len(wordDict) ≤ 1000`
#   - `1 ≤ len(wordDict[i]) ≤ 20`
#   - `s` și `wordDict[i]` conțin doar litere mici ale alfabetului englez
#   - Toate cuvintele din `wordDict` sunt distincte
#
# Teste:  python3 test.py 139      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
# @lc code=end
