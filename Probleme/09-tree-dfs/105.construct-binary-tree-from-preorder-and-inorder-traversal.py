#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Medium  ·  Trees — DFS
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Primești două array-uri de întregi, `preorder` și `inorder`: parcurgerea în preordine și
# parcurgerea în inordine ale aceluiași arbore binar. Reconstruiește arborele și returnează
# rădăcina lui.
#
# Exemplul 1
#   Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#   Output: [3,9,20,null,null,15,7]
#
# Exemplul 2
#   Input:  preorder = [-1], inorder = [-1]
#   Output: [-1]
#
# Constrângeri:
#   - `1 ≤ len(preorder) ≤ 3000`
#   - `len(inorder) == len(preorder)`
#   - `-3000 ≤ preorder[i], inorder[i] ≤ 3000`
#   - Valorile sunt distincte, iar cele două array-uri conțin aceleași valori
#   - `preorder` și `inorder` sunt parcurgeri valide ale aceluiași arbore
#
# Teste:  python3 test.py 105      (în VS Code: Cmd+Shift+B)
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
# @lc code=end
