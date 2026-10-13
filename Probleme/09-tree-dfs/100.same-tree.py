#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# Easy  ·  Trees — DFS
# https://leetcode.com/problems/same-tree/
#
# Primești rădăcinile a doi arbori binari, `p` și `q`. Returnează `True` dacă arborii sunt
# identici: au aceeași structură, iar nodurile corespondente au aceleași valori.
#
# Exemplul 1
#   Input:  p = [1,2,3], q = [1,2,3]
#   Output: true
#
# Exemplul 2
#   Input:  p = [1,2], q = [1,null,2]
#   Output: false
#
# Exemplul 3
#   Input:  p = [1,2,1], q = [1,1,2]
#   Output: false
#
# Constrângeri:
#   - Fiecare arbore are între 0 și 100 de noduri
#   - `-10⁴ ≤ Node.val ≤ 10⁴`
#
# Teste:  python3 test.py 100      (în VS Code: Cmd+Shift+B)
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
# @lc code=end
