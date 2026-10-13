#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# Medium  ·  Greedy
# https://leetcode.com/problems/jump-game/
#
# Primești un array de întregi `nums`. Pornești de pe primul index, iar fiecare element e lungimea
# maximă a saltului pe care îl poți face de pe acea poziție.
#
# Returnează `True` dacă poți ajunge la ultimul index și `False` altfel.
#
# Exemplul 1
#   Input:  nums = [2,3,1,1,4]
#   Output: true
#
# Exemplul 2
#   Input:  nums = [3,2,1,0,4]
#   Output: false
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁴`
#   - `0 ≤ nums[i] ≤ 10⁵`
#
# Teste:  python3 test.py 55      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
# @lc code=end
