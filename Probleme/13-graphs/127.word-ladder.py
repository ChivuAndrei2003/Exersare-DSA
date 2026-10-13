#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# Hard  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/word-ladder/
#
# O secvență de transformare de la cuvântul `beginWord` la cuvântul `endWord`, cu dicționarul
# `wordList`, e un șir de cuvinte `beginWord → s1 → s2 → … → sk` în care: oricare două cuvinte
# consecutive diferă printr-o singură literă; fiecare `s` se află în `wordList` (`beginWord` nu
# trebuie să fie în listă); iar `sk == endWord`.
#
# Returnează numărul de cuvinte din cea mai scurtă secvență de transformare sau 0 dacă nu există
# niciuna.
#
# Exemplul 1
#   Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
#   Output: 5
#
# Exemplul 2
#   Input:  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(beginWord) ≤ 10`
#   - `len(endWord) == len(beginWord)`
#   - `1 ≤ len(wordList) ≤ 5000`
#   - `len(wordList[i]) == len(beginWord)`
#   - Toate cuvintele conțin doar litere mici ale alfabetului englez
#   - `beginWord ≠ endWord`
#   - Toate cuvintele din `wordList` sunt distincte
#
# Teste:  python3 test.py 127      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
# @lc code=end
