#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# Hard  ·  Trees — DFS
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
# Un drum într-un arbore binar e o secvență de noduri în care oricare două noduri consecutive sunt
# legate printr-o muchie. Un nod apare cel mult o dată pe drum, iar drumul nu trebuie să treacă
# prin rădăcină. Suma drumului e suma valorilor nodurilor de pe el.
#
# Primești `root`, rădăcina unui arbore binar. Returnează suma maximă a unui drum nevid.
#
# Exemplul 1
#   Input:  root = [1,2,3]
#   Output: 6
#
# Exemplul 2
#   Input:  root = [-10,9,20,null,null,15,7]
#   Output: 42
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[1, 3 · 10⁴]`
#   - `-1000 ≤ Node.val ≤ 1000`
#
# Teste:  python3 test.py 124      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
# @lc code=end
