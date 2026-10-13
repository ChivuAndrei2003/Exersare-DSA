#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# Medium  ·  Linked List
# https://leetcode.com/problems/reorder-list/
#
# Primești capul unei liste simplu înlănțuite: L0 → L1 → … → Ln−1 → Ln. Reordoneaz-o astfel: L0 →
# Ln → L1 → Ln−1 → L2 → Ln−2 → …
#
# Nu ai voie să schimbi valorile din noduri, doar legăturile dintre ele. Funcția nu returnează
# nimic: modifică lista pe loc.
#
# Exemplul 1
#   Input:  head = [1,2,3,4]
#   Output: [1,4,2,3]
#
# Exemplul 2
#   Input:  head = [1,2,3,4,5]
#   Output: [1,5,2,4,3]
#
# Notă: Funcția modifică inputul pe loc; se verifică inputul după apel.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[1, 5 · 10⁴]`
#   - `1 ≤ Node.val ≤ 1000`
#
# Teste:  python3 test.py 143      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
# @lc code=end
