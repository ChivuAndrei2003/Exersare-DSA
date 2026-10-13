#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# Easy  ·  Linked List
# https://leetcode.com/problems/linked-list-cycle/
#
# Primești `head`, capul unei liste înlănțuite. Stabilește dacă lista are un ciclu. Există un
# ciclu dacă, urmând pointerii `next`, poți ajunge din nou la un nod deja vizitat.
#
# Returnează `True` dacă există un ciclu și `False` altfel. Follow-up: rezolvă cu memorie O(1).
#
# Exemplul 1
#   Input:  head = [3,2,0,-4], pos = 1
#   Output: true
#
# Exemplul 2
#   Input:  head = [1,2], pos = 0
#   Output: true
#
# Exemplul 3
#   Input:  head = [1], pos = -1
#   Output: false
#
# Notă: Inputul listei are și `pos`: indexul nodului în care se leagă coada (−1 = fără ciclu).
# Funcția ta primește doar `head`.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 10⁴]`
#   - `-10⁵ ≤ Node.val ≤ 10⁵`
#   - `pos` e −1 sau un index valid din listă
#
# Teste:  python3 test.py 141      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
# @lc code=end
