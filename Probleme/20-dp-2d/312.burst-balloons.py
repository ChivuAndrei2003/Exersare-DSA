#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# Hard  ·  Dynamic Programming — 2D
# https://leetcode.com/problems/burst-balloons/
#
# Ai `n` baloane, numerotate de la 0 la `n − 1`; pe fiecare e scris un număr, dat în array-ul
# `nums`. Trebuie să le spargi pe toate.
#
# Când spargi balonul `i`, primești `nums[i − 1] · nums[i] · nums[i + 1]` monede, unde vecinii
# sunt baloanele rămase lângă el în acel moment. Dacă `i − 1` sau `i + 1` iese din array, se
# consideră că acolo e un balon cu valoarea 1.
#
# Returnează numărul maxim de monede pe care le poți strânge, spărgând baloanele în cea mai bună
# ordine.
#
# Exemplul 1
#   Input:  nums = [3,1,5,8]
#   Output: 167
#
# Exemplul 2
#   Input:  nums = [1,5]
#   Output: 10
#
# Constrângeri:
#   - `n == len(nums)`
#   - `1 ≤ n ≤ 300`
#   - `0 ≤ nums[i] ≤ 100`
#
# Teste:  python3 test.py 312      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
# @lc code=end
