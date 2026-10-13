#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# Medium  ·  Greedy
# https://leetcode.com/problems/partition-labels/
#
# Primești un string `s`. Împarte-l în cât mai multe bucăți astfel încât fiecare literă să apară
# în cel mult o bucată. De exemplu, `"ababcc"` se poate împărți în `["abab", "cc"]`, dar nu în
# `["aba", "bcc"]`.
#
# Bucățile, concatenate în ordine, trebuie să dea exact `s`. Returnează lista lungimilor
# bucăților.
#
# Exemplul 1
#   Input:  s = "ababcbacadefegdehijhklij"
#   Output: [9,7,8]
#
# Exemplul 2
#   Input:  s = "eccbbbbdec"
#   Output: [10]
#
# Constrângeri:
#   - `1 ≤ len(s) ≤ 500`
#   - `s` conține doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 763      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
# @lc code=end
