#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# Medium  ·  Trees — DFS
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Primești un arbore binar de căutare (BST) și două noduri ale lui, `p` și `q`. Returnează cel mai
# jos strămoș comun (LCA) al lor.
#
# LCA-ul e cel mai adânc nod care îi are pe `p` și pe `q` ca descendenți. Un nod se consideră
# descendent al lui însuși, deci LCA-ul poate fi chiar `p` sau `q`.
#
# Exemplul 1
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#   Output: 6
#
# Exemplul 2
#   Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#   Output: 2
#
# Exemplul 3
#   Input:  root = [2,1], p = 2, q = 1
#   Output: 2
#
# Notă: `p` și `q` sunt valorile nodurilor; funcția ta primește nodurile propriu-zise și
# returnează nodul strămoș.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[2, 10⁵]`
#   - `-10⁹ ≤ Node.val ≤ 10⁹`
#   - Toate valorile `Node.val` sunt distincte
#   - `p ≠ q`
#   - `p` și `q` există în BST
#
# Teste:  python3 test.py 235      (în VS Code: Cmd+Shift+B)
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
# @lc code=end
