#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# Easy  ·  Sliding Window
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Primești un array `prices`, unde `prices[i]` e prețul unei acțiuni în ziua `i`.
#
# Vrei profitul maxim alegând o singură zi în care cumperi și o zi ulterioară în care vinzi.
# Returnează profitul maxim; dacă nu poți obține profit, returnează 0.
#
# Exemplul 1
#   Input:  prices = [7,1,5,3,6,4]
#   Output: 5
#
# Exemplul 2
#   Input:  prices = [7,6,4,3,1]
#   Output: 0
#
# Constrângeri:
#   - `1 ≤ len(prices) ≤ 10⁵`
#   - `0 ≤ prices[i] ≤ 10⁴`
#
# Teste:  python3 test.py 121      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
# @lc code=end
