#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# Medium  ·  Union-Find (DSU)
# https://leetcode.com/problems/number-of-provinces/
#
# Există `n` orașe; unele sunt conectate direct, altele nu. Dacă orașul `a` e conectat direct cu
# `b`, iar `b` cu `c`, atunci `a` e conectat indirect cu `c`. O provincie e un grup de orașe
# conectate direct sau indirect, fără niciun alt oraș din afara grupului.
#
# Primești matricea `isConnected` de n × n: `isConnected[i][j] = 1` dacă orașele `i` și `j` sunt
# conectate direct și 0 altfel. Returnează numărul de provincii.
#
# Exemplul 1
#   Input:  isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#   Output: 2
#
# Exemplul 2
#   Input:  isConnected = [[1,0,0],[0,1,0],[0,0,1]]
#   Output: 3
#
# Constrângeri:
#   - `1 ≤ n ≤ 200`
#   - `n == len(isConnected) == len(isConnected[i])`
#   - `isConnected[i][j]` e 1 sau 0
#   - `isConnected[i][i] == 1`
#   - `isConnected[i][j] == isConnected[j][i]`
#
# Teste:  python3 test.py 547      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
# @lc code=end
