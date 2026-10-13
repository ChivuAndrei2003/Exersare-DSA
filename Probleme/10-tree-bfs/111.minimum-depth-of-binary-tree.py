#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Easy  ·  Trees — BFS
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
#
# Primești `root`, rădăcina unui arbore binar. Returnează adâncimea minimă: numărul de noduri de
# pe cel mai scurt drum de la rădăcină până la cea mai apropiată frunză.
#
# O frunză e un nod fără copii. Pentru un arbore gol răspunsul e 0.
#
# Exemplul 1
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: 2
#
# Exemplul 2
#   Input:  root = [2,null,3,null,4,null,5,null,6]
#   Output: 5
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 10⁵]`
#   - `-1000 ≤ Node.val ≤ 1000`
#
# Teste:  python3 test.py 111      (în VS Code: Cmd+Shift+B)
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
# @lc code=end
