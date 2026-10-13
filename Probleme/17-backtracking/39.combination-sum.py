#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/combination-sum/
#
# Primești un array de întregi distincți, `candidates`, și un întreg `target`. Returnează toate
# combinațiile unice de numere din `candidates` a căror sumă e `target`, în orice ordine.
#
# Același număr poate fi folosit de oricâte ori. Două combinații sunt diferite dacă măcar un număr
# apare de un număr diferit de ori. Testele sunt alese astfel încât să existe mai puțin de 150 de
# combinații.
#
# Exemplul 1
#   Input:  candidates = [2,3,6,7], target = 7
#   Output: [[2,2,3],[7]]
#
# Exemplul 2
#   Input:  candidates = [2,3,5], target = 8
#   Output: [[2,2,2,2],[2,3,3],[3,5]]
#
# Exemplul 3
#   Input:  candidates = [2], target = 1
#   Output: []
#
# Notă: Ordinea nu contează (nici în listă, nici în interiorul grupurilor).
#
# Constrângeri:
#   - `1 ≤ len(candidates) ≤ 30`
#   - `2 ≤ candidates[i] ≤ 40`
#   - Toate elementele din `candidates` sunt distincte
#   - `1 ≤ target ≤ 40`
#
# Teste:  python3 test.py 39      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
# @lc code=end
