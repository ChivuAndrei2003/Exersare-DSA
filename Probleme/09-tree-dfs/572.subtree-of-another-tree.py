#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# Easy  ·  Trees — DFS
# https://leetcode.com/problems/subtree-of-another-tree/
#
# Primești rădăcinile a doi arbori binari, `root` și `subRoot`. Returnează `True` dacă `root` are
# un subarbore cu aceeași structură și aceleași valori ca `subRoot` și `False` altfel.
#
# Un subarbore e format dintr-un nod și toți descendenții lui. Arborele întreg e și el un
# subarbore al lui însuși.
#
# Exemplul 1
#   Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
#   Output: true
#
# Exemplul 2
#   Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#   Output: false
#
# Constrângeri:
#   - `root` are între 1 și 2000 de noduri
#   - `subRoot` are între 1 și 1000 de noduri
#   - `-10⁴ ≤ root.val ≤ 10⁴`
#   - `-10⁴ ≤ subRoot.val ≤ 10⁴`
#
# Teste:  python3 test.py 572      (în VS Code: Cmd+Shift+B)
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
# @lc code=end
