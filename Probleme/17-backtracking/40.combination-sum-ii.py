#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/combination-sum-ii/
#
# Primești o colecție de numere, `candidates` (pot exista duplicate), și un întreg `target`.
# Returnează toate combinațiile unice de numere din `candidates` a căror sumă e `target`.
#
# Fiecare element din `candidates` poate fi folosit o singură dată într-o combinație. Rezultatul
# nu trebuie să conțină combinații duplicate.
#
# Exemplul 1
#   Input:  candidates = [10,1,2,7,6,1,5], target = 8
#   Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
#
# Exemplul 2
#   Input:  candidates = [2,5,2,1,2], target = 5
#   Output: [[1,2,2],[5]]
#
# Notă: Ordinea nu contează (nici în listă, nici în interiorul grupurilor).
#
# Constrângeri:
#   - `1 ≤ len(candidates) ≤ 100`
#   - `1 ≤ candidates[i] ≤ 50`
#   - `1 ≤ target ≤ 30`
#
# Teste:  python3 test.py 40      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
# @lc code=end
