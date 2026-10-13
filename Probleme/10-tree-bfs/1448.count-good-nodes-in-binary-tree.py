#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#
# Medium  ·  Trees — BFS
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# Primești `root`, rădăcina unui arbore binar. Un nod `X` e bun dacă pe drumul de la rădăcină până
# la `X` nu există niciun nod cu valoare mai mare decât a lui `X`.
#
# Returnează numărul de noduri bune. Rădăcina e mereu un nod bun.
#
# Exemplul 1
#   Input:  root = [3,1,4,3,null,1,5]
#   Output: 4
#
# Exemplul 2
#   Input:  root = [3,3,null,4,2]
#   Output: 3
#
# Exemplul 3
#   Input:  root = [1]
#   Output: 1
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[1, 10⁵]`
#   - `-10⁴ ≤ Node.val ≤ 10⁴`
#
# Teste:  python3 test.py 1448      (în VS Code: Cmd+Shift+B)
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
    def goodNodes(self, root: TreeNode) -> int:
        
# @lc code=end
