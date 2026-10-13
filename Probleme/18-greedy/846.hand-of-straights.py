#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# Medium  ·  Greedy
# https://leetcode.com/problems/hand-of-straights/
#
# Alice are un număr de cărți și vrea să le aranjeze în grupuri, fiecare cu exact `groupSize`
# cărți cu valori consecutive.
#
# Primești `hand`, unde `hand[i]` e valoarea scrisă pe cartea `i`, și întregul `groupSize`.
# Returnează `True` dacă își poate aranja toate cărțile astfel și `False` altfel.
#
# Exemplul 1
#   Input:  hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
#   Output: true
#
# Exemplul 2
#   Input:  hand = [1,2,3,4,5], groupSize = 4
#   Output: false
#
# Constrângeri:
#   - `1 ≤ len(hand) ≤ 10⁴`
#   - `0 ≤ hand[i] ≤ 10⁹`
#   - `1 ≤ groupSize ≤ len(hand)`
#
# Teste:  python3 test.py 846      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
# @lc code=end
