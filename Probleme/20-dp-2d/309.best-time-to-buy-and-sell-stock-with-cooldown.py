#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# Medium  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
#
# Primești un array `prices`, unde `prices[i]` e prețul unei acțiuni în ziua `i`. Găsește profitul
# maxim. Poți face oricâte tranzacții (cumperi o acțiune, apoi o vinzi), cu două restricții.
#
# După ce vinzi, nu poți cumpăra în ziua următoare (o zi de cooldown). Și nu poți avea mai multe
# tranzacții în același timp: trebuie să vinzi acțiunea înainte să cumperi din nou.
#
# Exemplul 1
#   Input:  prices = [1,2,3,0,2]
#   Output: 3
#
# Exemplul 2
#   Input:  prices = [1]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(prices) ≤ 5000`
#   - `0 ≤ prices[i] ≤ 1000`
#
# Teste:  python3 test.py 309      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
# @lc code=end
