#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/house-robber/
#
# Ești un hoț care plănuiește să jefuiască casele de pe o stradă; casa `i` are `nums[i]` bani.
# Singura restricție: casele vecine au alarmele legate între ele, iar alarma sună dacă două case
# alăturate sunt sparte în aceeași noapte.
#
# Returnează suma maximă pe care o poți fura într-o noapte fără să declanșezi alarma.
#
# Exemplul 1
#   Input:  nums = [1,2,3,1]
#   Output: 4
#
# Exemplul 2
#   Input:  nums = [2,7,9,3,1]
#   Output: 12
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 100`
#   - `0 ≤ nums[i] ≤ 400`
#
# Teste:  python3 test.py 198      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
# @lc code=end
