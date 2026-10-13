#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# Easy  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/min-cost-climbing-stairs/
#
# Primești un array `cost`, unde `cost[i]` e costul treptei `i` a unei scări. După ce plătești
# costul unei trepte, poți urca una sau două trepte.
#
# Poți porni de pe treapta cu indexul 0 sau de pe cea cu indexul 1. Returnează costul minim cu
# care ajungi în vârf, adică dincolo de ultima treaptă.
#
# Exemplul 1
#   Input:  cost = [10,15,20]
#   Output: 15
#
# Exemplul 2
#   Input:  cost = [1,100,1,1,1,100,1,1,100,1]
#   Output: 6
#
# Constrângeri:
#   - `2 ≤ len(cost) ≤ 1000`
#   - `0 ≤ cost[i] ≤ 999`
#
# Teste:  python3 test.py 746      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
# @lc code=end
