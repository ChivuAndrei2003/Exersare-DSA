#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
# Medium  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/car-fleet/
#
# `n` mașini merg pe un drum cu o singură bandă spre o destinație aflată la kilometrul `target`.
# Mașina `i` pornește din `position[i]` și are viteza `speed[i]`.
#
# O mașină nu poate depăși: când o ajunge din urmă pe cea din față, încetinește și merg mai
# departe împreună, cu viteza celei mai lente. O flotă e un grup nevid de mașini care merg în
# aceeași poziție și cu aceeași viteză; o singură mașină e tot o flotă. Dacă o mașină ajunge din
# urmă o flotă exact la destinație, face parte din ea.
#
# Returnează numărul de flote care ajung la destinație.
#
# Exemplul 1
#   Input:  target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
#   Output: 3
#
# Exemplul 2
#   Input:  target = 10, position = [3], speed = [3]
#   Output: 1
#
# Exemplul 3
#   Input:  target = 100, position = [0,2,4], speed = [4,2,1]
#   Output: 1
#
# Constrângeri:
#   - `n == len(position) == len(speed)`
#   - `1 ≤ n ≤ 10⁵`
#   - `0 < target ≤ 10⁶`
#   - `0 ≤ position[i] < target`
#   - Toate valorile din `position` sunt distincte
#   - `0 < speed[i] ≤ 10⁶`
#
# Teste:  python3 test.py 853      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
# @lc code=end
