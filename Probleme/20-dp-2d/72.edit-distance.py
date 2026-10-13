#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/edit-distance/
#
# Primești două stringuri, `word1` și `word2`. Returnează numărul minim de operații necesare ca să
# transformi `word1` în `word2`.
#
# Ai trei operații, fiecare aplicată unui singur caracter: inserare, ștergere și înlocuire.
#
# Exemplul 1
#   Input:  word1 = "horse", word2 = "ros"
#   Output: 3
#
# Exemplul 2
#   Input:  word1 = "intention", word2 = "execution"
#   Output: 5
#
# Constrângeri:
#   - `0 ≤ len(word1), len(word2) ≤ 500`
#   - `word1` și `word2` conțin doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 72      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
# @lc code=end
