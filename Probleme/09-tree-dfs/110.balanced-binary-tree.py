#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Easy  ·  Trees — DFS
# https://leetcode.com/problems/balanced-binary-tree/
#
# Primești `root`, rădăcina unui arbore binar. Stabilește dacă arborele e echilibrat pe înălțime:
# la fiecare nod, înălțimea subarborelui stâng și cea a subarborelui drept diferă cu cel mult 1.
#
# Exemplul 1
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: true
#
# Exemplul 2
#   Input:  root = [1,2,2,3,3,null,null,4,4]
#   Output: false
#
# Exemplul 3
#   Input:  root = []
#   Output: true
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 5000]`
#   - `-10⁴ ≤ Node.val ≤ 10⁴`
#
# Teste:  python3 test.py 110      (în VS Code: Cmd+Shift+B)
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
# @lc code=end
