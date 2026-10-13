#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Easy  ·  Trees — DFS
# https://leetcode.com/problems/invert-binary-tree/
#
# Primești `root`, rădăcina unui arbore binar. Inversează arborele — la fiecare nod, schimbă între
# ei subarborele stâng și cel drept — și returnează rădăcina.
#
# Exemplul 1
#   Input:  root = [4,2,7,1,3,6,9]
#   Output: [4,7,2,9,6,3,1]
#
# Exemplul 2
#   Input:  root = [2,1,3]
#   Output: [2,3,1]
#
# Exemplul 3
#   Input:  root = []
#   Output: []
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 100]`
#   - `-100 ≤ Node.val ≤ 100`
#
# Teste:  python3 test.py 226      (în VS Code: Cmd+Shift+B)
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
# @lc code=end
