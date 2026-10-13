#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# Hard  ·  Binary Search
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Primești două array-uri sortate, `nums1` (de lungime m) și `nums2` (de lungime n). Returnează
# mediana tuturor elementelor din cele două array-uri: elementul din mijloc dacă numărul total e
# impar, media celor două din mijloc dacă e par.
#
# Complexitatea trebuie să fie O(log(m + n)).
#
# Exemplul 1
#   Input:  nums1 = [1,3], nums2 = [2]
#   Output: 2
#
# Exemplul 2
#   Input:  nums1 = [1,2], nums2 = [3,4]
#   Output: 2.5
#
# Notă: Răspunsurile se acceptă cu o eroare de până la 10⁻⁵.
#
# Constrângeri:
#   - `m == len(nums1)`, `n == len(nums2)`
#   - `0 ≤ m ≤ 1000`, `0 ≤ n ≤ 1000`
#   - `1 ≤ m + n ≤ 2000`
#   - `-10⁶ ≤ nums1[i], nums2[i] ≤ 10⁶`
#
# Teste:  python3 test.py 4      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
# @lc code=end
