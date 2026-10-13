#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# Hard  ·  Trees — BFS
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#
# Serializarea transformă o structură de date într-un șir de caractere care poate fi stocat sau
# transmis și apoi reconstruit. Proiectează un algoritm care serializează și deserializează un
# arbore binar.
#
# Implementează clasa `Codec`: `serialize(root)` primește rădăcina și returnează un string, iar
# `deserialize(data)` primește acel string și reconstruiește arborele. Formatul stringului e la
# alegerea ta; singura cerință e ca `deserialize(serialize(root))` să dea un arbore identic cu
# originalul.
#
# Exemplul 1
#   Input:  root = [1,2,3,null,null,4,5]
#   Output: [1,2,3,null,null,4,5]
#
# Exemplul 2
#   Input:  root = []
#   Output: []
#
# Notă: Se verifică `deserialize(serialize(root))`: trebuie să obții același arbore.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 10⁴]`
#   - `-1000 ≤ Node.val ≤ 1000`
#
# Teste:  python3 test.py 297      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
