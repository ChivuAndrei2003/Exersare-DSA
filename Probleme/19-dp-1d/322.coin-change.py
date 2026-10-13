#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/coin-change/
#
# Primești un array `coins` cu valorile unor tipuri de monede și un întreg `amount`, o sumă de
# bani. Din fiecare tip ai oricâte monede.
#
# Returnează numărul minim de monede cu care poți forma exact suma `amount`. Dacă suma nu poate fi
# formată, returnează −1.
#
# Exemplul 1
#   Input:  coins = [1,2,5], amount = 11
#   Output: 3
#
# Exemplul 2
#   Input:  coins = [2], amount = 3
#   Output: -1
#
# Exemplul 3
#   Input:  coins = [1], amount = 0
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(coins) ≤ 12`
#   - `1 ≤ coins[i] ≤ 2³¹ − 1`
#   - `0 ≤ amount ≤ 10⁴`
#
# Teste:  python3 test.py 322      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
# @lc code=end
