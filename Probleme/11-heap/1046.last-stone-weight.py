#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
# Easy  ·  Heap / Top K
# https://leetcode.com/problems/last-stone-weight/
#
# Primești un array `stones`, unde `stones[i]` e greutatea pietrei `i`. La fiecare tură iei cele
# mai grele două pietre, cu greutățile `x ≤ y`, și le ciocnești.
#
# Dacă `x == y`, ambele pietre se distrug. Dacă `x ≠ y`, piatra `x` se distruge, iar piatra `y`
# rămâne cu greutatea `y − x`.
#
# Jocul se termină când rămâne cel mult o piatră. Returnează greutatea ei sau 0 dacă nu mai rămâne
# niciuna.
#
# Exemplul 1
#   Input:  stones = [2,7,4,1,8,1]
#   Output: 1
#
# Exemplul 2
#   Input:  stones = [1]
#   Output: 1
#
# Constrângeri:
#   - `1 ≤ len(stones) ≤ 30`
#   - `1 ≤ stones[i] ≤ 1000`
#
# Teste:  python3 test.py 1046      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
# @lc code=end
