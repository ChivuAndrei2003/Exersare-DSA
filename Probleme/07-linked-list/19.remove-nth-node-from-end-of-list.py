#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Medium  ·  Linked List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Primești `head`, capul unei liste înlănțuite, și un întreg `n`. Șterge al `n`-lea nod numărat de
# la finalul listei și returnează capul listei.
#
# Follow-up: rezolvă într-o singură trecere.
#
# Exemplul 1
#   Input:  head = [1,2,3,4,5], n = 2
#   Output: [1,2,3,5]
#
# Exemplul 2
#   Input:  head = [1], n = 1
#   Output: []
#
# Exemplul 3
#   Input:  head = [1,2], n = 1
#   Output: [1]
#
# Constrângeri:
#   - Numărul de noduri este `sz`
#   - `1 ≤ sz ≤ 30`
#   - `0 ≤ Node.val ≤ 100`
#   - `1 ≤ n ≤ sz`
#
# Teste:  python3 test.py 19      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
# @lc code=end
