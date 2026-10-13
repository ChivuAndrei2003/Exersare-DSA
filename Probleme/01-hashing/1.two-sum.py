#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# Easy  ·  Arrays & Hashing
# https://leetcode.com/problems/two-sum/
#
# Primești un array de întregi `nums` și un întreg `target`. Returnează indicii celor două numere
# a căror sumă e `target`.
#
# Există exact o soluție și nu ai voie să folosești același element de două ori. Indicii pot fi
# returnați în orice ordine.
#
# Follow-up: găsește un algoritm mai rapid decât O(n²).
#
# Exemplul 1
#   Input:  nums = [2,7,11,15], target = 9
#   Output: [0,1]
#
# Exemplul 2
#   Input:  nums = [3,2,4], target = 6
#   Output: [1,2]
#
# Exemplul 3
#   Input:  nums = [3,3], target = 6
#   Output: [0,1]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `2 ≤ len(nums) ≤ 10⁴`
#   - `-10⁹ ≤ nums[i] ≤ 10⁹`
#   - `-10⁹ ≤ target ≤ 10⁹`
#   - Există exact un răspuns valid
#
# Teste:  python3 test.py 1      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # type: ignore
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
        return []


# @lc code=end
