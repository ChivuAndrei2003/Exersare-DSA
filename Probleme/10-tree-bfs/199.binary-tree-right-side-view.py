#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# Medium  ·  Trees — BFS
# https://leetcode.com/problems/binary-tree-right-side-view/
#
# Primești `root`, rădăcina unui arbore binar. Imaginează-ți că privești arborele din partea
# dreaptă: returnează valorile nodurilor pe care le vezi, de sus în jos (de pe fiecare nivel se
# vede doar nodul cel mai din dreapta).
#
# Exemplul 1
#   Input:  root = [1,2,3,null,5,null,4]
#   Output: [1,3,4]
#
# Exemplul 2
#   Input:  root = [1,2,3,4,null,null,null,5]
#   Output: [1,3,4,5]
#
# Exemplul 3
#   Input:  root = [1,null,3]
#   Output: [1,3]
#
# Exemplul 4
#   Input:  root = []
#   Output: []
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 100]`
#   - `-100 ≤ Node.val ≤ 100`
#
# Teste:  python3 test.py 199      (în VS Code: Cmd+Shift+B)
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
# @lc code=end
