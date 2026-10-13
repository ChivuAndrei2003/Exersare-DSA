#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Medium  ·  Trees — DFS
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# Primești un arbore binar oarecare și două noduri ale lui, `p` și `q`. Returnează cel mai jos
# strămoș comun (LCA) al lor.
#
# LCA-ul e cel mai adânc nod care îi are pe `p` și pe `q` ca descendenți. Un nod se consideră
# descendent al lui însuși, deci LCA-ul poate fi chiar `p` sau `q`.
#
# Exemplul 1
#   Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#   Output: 3
#
# Exemplul 2
#   Input:  root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#   Output: 5
#
# Exemplul 3
#   Input:  root = [1,2], p = 1, q = 2
#   Output: 1
#
# Notă: `p` și `q` sunt valorile nodurilor; funcția ta primește nodurile propriu-zise și
# returnează nodul strămoș.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[2, 10⁵]`
#   - `-10⁹ ≤ Node.val ≤ 10⁹`
#   - Toate valorile `Node.val` sunt distincte
#   - `p ≠ q`
#   - `p` și `q` există în arbore
#
# Teste:  python3 test.py 236      (în VS Code: Cmd+Shift+B)
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
