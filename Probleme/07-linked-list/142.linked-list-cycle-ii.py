#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# Medium  ·  Linked List
# https://leetcode.com/problems/linked-list-cycle-ii/
#
# Primești `head`, capul unei liste înlănțuite. Returnează nodul în care începe ciclul sau `None`
# dacă lista nu are ciclu.
#
# Există un ciclu dacă, urmând pointerii `next`, poți ajunge din nou la un nod deja vizitat. Nu
# modifica lista. Follow-up: rezolvă cu memorie O(1).
#
# Exemplul 1
#   Input:  head = [3,2,0,-4], pos = 1
#   Output: 1
#
# Exemplul 2
#   Input:  head = [1,2], pos = 0
#   Output: 0
#
# Exemplul 3
#   Input:  head = [1], pos = -1
#   Output: -1
#
# Notă: Inputul listei are și `pos`: indexul nodului în care se leagă coada (−1 = fără ciclu).
# Funcția ta primește doar `head`.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 10⁴]`
#   - `-10⁵ ≤ Node.val ≤ 10⁵`
#   - `pos` e −1 sau un index valid din listă
#
# Teste:  python3 test.py 142      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
# @lc code=end
