#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/coin-change-ii/
#
# Primești un array `coins` cu valorile unor tipuri de monede și un întreg `amount`. Din fiecare
# tip ai oricâte monede.
#
# Returnează numărul de combinații de monede care formează exact suma `amount` (ordinea monedelor
# nu contează) sau 0 dacă suma nu poate fi formată. Răspunsul încape pe 32 de biți.
#
# Exemplul 1
#   Input:  amount = 5, coins = [1,2,5]
#   Output: 4
#
# Exemplul 2
#   Input:  amount = 3, coins = [2]
#   Output: 0
#
# Exemplul 3
#   Input:  amount = 10, coins = [10]
#   Output: 1
#
# Constrângeri:
#   - `1 ≤ len(coins) ≤ 300`
#   - `1 ≤ coins[i] ≤ 5000`
#   - Toate valorile din `coins` sunt distincte
#   - `0 ≤ amount ≤ 5000`
#
# Teste:  python3 test.py 518      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
# @lc code=end
