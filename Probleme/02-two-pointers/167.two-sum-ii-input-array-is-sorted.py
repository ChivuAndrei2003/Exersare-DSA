#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# Medium  ·  Two Pointers
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
# Primești un array de întregi `numbers`, indexat de la 1 și sortat crescător, și un întreg
# `target`. Găsește două numere a căror sumă e `target` și returnează indicii lor, `[index1,
# index2]`, cu `1 ≤ index1 < index2 ≤ len(numbers)`.
#
# Există exact o soluție și nu ai voie să folosești același element de două ori. Soluția trebuie
# să folosească doar memorie suplimentară constantă.
#
# Exemplul 1
#   Input:  numbers = [2,7,11,15], target = 9
#   Output: [1,2]
#
# Exemplul 2
#   Input:  numbers = [2,3,4], target = 6
#   Output: [1,3]
#
# Exemplul 3
#   Input:  numbers = [-1,0], target = -1
#   Output: [1,2]
#
# Constrângeri:
#   - `2 ≤ len(numbers) ≤ 3 · 10⁴`
#   - `-1000 ≤ numbers[i] ≤ 1000`
#   - `numbers` e sortat crescător (nedescrescător)
#   - `-1000 ≤ target ≤ 1000`
#   - Există exact o soluție
#
# Teste:  python3 test.py 167      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
# @lc code=end
