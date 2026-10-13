#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# Easy  ·  Two Pointers
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Primești un array `nums` sortat crescător. Elimină duplicatele in-place, astfel încât fiecare
# valoare să apară o singură dată, păstrând ordinea. Returnează `k`, numărul de valori distincte.
#
# După apel, primele `k` poziții din `nums` trebuie să conțină valorile distincte, în ordinea
# inițială. Ce rămâne după ele nu contează.
#
# Exemplul 1
#   Input:  nums = [1,1,2]
#   Output: [2,[1,2]]
#
# Exemplul 2
#   Input:  nums = [0,0,1,1,1,2,2,3,3,4]
#   Output: [5,[0,1,2,3,4]]
#
# Notă: Se verifică `k` și primele `k` elemente din `nums` după apel.
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 3 · 10⁴`
#   - `-100 ≤ nums[i] ≤ 100`
#   - `nums` e sortat crescător (nedescrescător)
#
# Teste:  python3 test.py 26      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
# @lc code=end
