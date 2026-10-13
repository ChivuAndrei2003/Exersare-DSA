#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Hard  ·  Heap / Top K
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# Primești `lists`, un array cu `k` liste înlănțuite, fiecare sortată crescător. Unește-le într-o
# singură listă sortată și returneaz-o.
#
# Exemplul 1
#   Input:  lists = [[1,4,5],[1,3,4],[2,6]]
#   Output: [1,1,2,3,4,4,5,6]
#
# Exemplul 2
#   Input:  lists = []
#   Output: []
#
# Exemplul 3
#   Input:  lists = [[]]
#   Output: []
#
# Constrângeri:
#   - `k == len(lists)`
#   - `0 ≤ k ≤ 10⁴`
#   - Fiecare listă are între 0 și 500 de noduri
#   - `-10⁴ ≤ Node.val ≤ 10⁴`
#   - Fiecare listă e sortată crescător
#   - În total sunt cel mult 10⁴ noduri
#
# Teste:  python3 test.py 23      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
# @lc code=end
