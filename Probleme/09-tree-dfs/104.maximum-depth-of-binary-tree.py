#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# Easy  ·  Trees — DFS
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Primești `root`, rădăcina unui arbore binar. Returnează adâncimea maximă: numărul de noduri de
# pe cel mai lung drum de la rădăcină până la cea mai îndepărtată frunză. Un arbore gol are
# adâncimea 0.
#
# Exemplul 1
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: 3
#
# Exemplul 2
#   Input:  root = [1,null,2]
#   Output: 2
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 10⁴]`
#   - `-100 ≤ Node.val ≤ 100`
#
# Teste:  python3 test.py 104      (în VS Code: Cmd+Shift+B)
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
# @lc code=end
