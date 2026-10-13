#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# Medium  ·  Trees — DFS
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#
# Primești `root`, rădăcina unui arbore binar de căutare, și un întreg `k`. Returnează a `k`-a cea
# mai mică valoare din arbore (numărând de la 1).
#
# Follow-up: dacă arborele se modifică des (inserări, ștergeri) și ai nevoie des de al k-lea
# element, cum ai optimiza?
#
# Exemplul 1
#   Input:  root = [3,1,4,null,2], k = 1
#   Output: 1
#
# Exemplul 2
#   Input:  root = [5,3,6,2,4,null,null,1], k = 3
#   Output: 3
#
# Constrângeri:
#   - Numărul de noduri este `n`
#   - `1 ≤ k ≤ n ≤ 10⁴`
#   - `0 ≤ Node.val ≤ 10⁴`
#
# Teste:  python3 test.py 230      (în VS Code: Cmd+Shift+B)
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
# @lc code=end
