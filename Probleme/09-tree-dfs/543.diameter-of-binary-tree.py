#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Easy  ·  Trees — DFS
# https://leetcode.com/problems/diameter-of-binary-tree/
#
# Primești `root`, rădăcina unui arbore binar. Returnează diametrul arborelui: lungimea celui mai
# lung drum dintre oricare două noduri. Drumul poate să treacă sau nu prin rădăcină.
#
# Lungimea unui drum se măsoară în muchii.
#
# Exemplul 1
#   Input:  root = [1,2,3,4,5]
#   Output: 3
#
# Exemplul 2
#   Input:  root = [1,2]
#   Output: 1
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[1, 10⁴]`
#   - `-100 ≤ Node.val ≤ 100`
#
# Teste:  python3 test.py 543      (în VS Code: Cmd+Shift+B)
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
# @lc code=end
