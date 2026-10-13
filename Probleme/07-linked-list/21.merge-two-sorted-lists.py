#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Easy  ·  Linked List
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Primești capetele a două liste înlănțuite sortate, `list1` și `list2`. Unește-le într-o singură
# listă sortată, construită prin legarea nodurilor celor două liste, și returnează capul ei.
#
# Exemplul 1
#   Input:  list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]
#
# Exemplul 2
#   Input:  list1 = [], list2 = []
#   Output: []
#
# Exemplul 3
#   Input:  list1 = [], list2 = [0]
#   Output: [0]
#
# Constrângeri:
#   - Fiecare listă are între 0 și 50 de noduri
#   - `-100 ≤ Node.val ≤ 100`
#   - `list1` și `list2` sunt sortate crescător (nedescrescător)
#
# Teste:  python3 test.py 21      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
# @lc code=end
