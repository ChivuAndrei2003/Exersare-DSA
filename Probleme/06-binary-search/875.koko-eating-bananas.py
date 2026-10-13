#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# Medium  ·  Binary Search
# https://leetcode.com/problems/koko-eating-bananas/
#
# Koko are `n` grămezi de banane; grămada `i` are `piles[i]` banane. Paznicii se întorc peste `h`
# ore.
#
# Koko își alege o viteză `k` (banane pe oră). În fiecare oră alege o grămadă și mănâncă `k`
# banane din ea; dacă grămada are mai puține, le mănâncă pe toate și nu mai mănâncă nimic în ora
# aceea.
#
# Returnează cel mai mic `k` întreg cu care termină toate bananele în cel mult `h` ore.
#
# Exemplul 1
#   Input:  piles = [3,6,7,11], h = 8
#   Output: 4
#
# Exemplul 2
#   Input:  piles = [30,11,23,4,20], h = 5
#   Output: 30
#
# Exemplul 3
#   Input:  piles = [30,11,23,4,20], h = 6
#   Output: 23
#
# Constrângeri:
#   - `1 ≤ len(piles) ≤ 10⁴`
#   - `len(piles) ≤ h ≤ 10⁹`
#   - `1 ≤ piles[i] ≤ 10⁹`
#
# Teste:  python3 test.py 875      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
# @lc code=end
