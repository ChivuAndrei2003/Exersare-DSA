#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Easy  ·  Linked List
# https://leetcode.com/problems/reverse-linked-list/
#
# Primești `head`, capul unei liste simplu înlănțuite. Inversează lista și returnează capul listei
# inversate.
#
# Follow-up: rezolvă atât iterativ, cât și recursiv.
#
# Exemplul 1
#   Input:  head = [1,2,3,4,5]
#   Output: [5,4,3,2,1]
#
# Exemplul 2
#   Input:  head = [1,2]
#   Output: [2,1]
#
# Exemplul 3
#   Input:  head = []
#   Output: []
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 5000]`
#   - `-5000 ≤ Node.val ≤ 5000`
#
# Teste:  python3 test.py 206      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
# @lc code=end
