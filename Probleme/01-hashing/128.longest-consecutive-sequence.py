#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# Medium  ·  Arrays & Hashing
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Primești un array nesortat de întregi, `nums`. Returnează lungimea celei mai lungi secvențe de
# numere consecutive (de exemplu 1, 2, 3, 4) care se poate forma cu valori din array. Elementele
# nu trebuie să fie vecine în `nums`.
#
# Algoritmul trebuie să ruleze în O(n).
#
# Exemplul 1
#   Input:  nums = [100,4,200,1,3,2]
#   Output: 4
#
# Exemplul 2
#   Input:  nums = [0,3,7,2,5,8,4,6,0,1]
#   Output: 9
#
# Exemplul 3
#   Input:  nums = [1,0,1,2]
#   Output: 3
#
# Constrângeri:
#   - `0 ≤ len(nums) ≤ 10⁵`
#   - `-10⁹ ≤ nums[i] ≤ 10⁹`
#
# Teste:  python3 test.py 128      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
# @lc code=end
