#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Medium  ·  Trees — BFS
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Primești `root`, rădăcina unui arbore binar. Returnează parcurgerea pe niveluri în zigzag:
# primul nivel de la stânga la dreapta, următorul de la dreapta la stânga și tot așa, alternând.
#
# Exemplul 1
#   Input:  root = [3,9,20,null,null,15,7]
#   Output: [[3],[20,9],[15,7]]
#
# Exemplul 2
#   Input:  root = [1]
#   Output: [[1]]
#
# Exemplul 3
#   Input:  root = []
#   Output: []
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 2000]`
#   - `-100 ≤ Node.val ≤ 100`
#
# Teste:  python3 test.py 103      (în VS Code: Cmd+Shift+B)
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
# @lc code=end
