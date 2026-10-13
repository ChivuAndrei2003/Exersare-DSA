#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Medium  ·  Trees — DFS
# https://leetcode.com/problems/validate-binary-search-tree/
#
# Primești `root`, rădăcina unui arbore binar. Stabilește dacă e un arbore binar de căutare (BST)
# valid.
#
# Un BST valid respectă trei reguli: subarborele stâng al unui nod conține doar valori strict mai
# mici decât nodul; subarborele drept conține doar valori strict mai mari; ambii subarbori sunt la
# rândul lor BST-uri valide.
#
# Exemplul 1
#   Input:  root = [2,1,3]
#   Output: true
#
# Exemplul 2
#   Input:  root = [5,1,4,null,null,3,6]
#   Output: false
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[1, 10⁴]`
#   - `-2³¹ ≤ Node.val ≤ 2³¹ − 1`
#
# Teste:  python3 test.py 98      (în VS Code: Cmd+Shift+B)
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
# @lc code=end
