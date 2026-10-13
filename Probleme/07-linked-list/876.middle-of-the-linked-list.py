#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# Easy  ·  Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
#
# Primești `head`, capul unei liste simplu înlănțuite. Returnează nodul din mijlocul listei.
#
# Dacă lista are două noduri de mijloc (număr par de noduri), returnează-l pe al doilea.
#
# Exemplul 1
#   Input:  head = [1,2,3,4,5]
#   Output: [3,4,5]
#
# Exemplul 2
#   Input:  head = [1,2,3,4,5,6]
#   Output: [4,5,6]
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[1, 100]`
#   - `1 ≤ Node.val ≤ 100`
#
# Teste:  python3 test.py 876      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
# @lc code=end
