#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# Easy  ·  Prefix Sum
# https://leetcode.com/problems/range-sum-query-immutable/
#
# Primești un array de întregi `nums` și trebuie să răspunzi la multe interogări de forma: care e
# suma elementelor dintre indicii `left` și `right`, inclusiv?
#
# Implementează clasa `NumArray`: constructorul `NumArray(nums)` primește array-ul, iar
# `sumRange(left, right)` returnează `nums[left] + nums[left + 1] + … + nums[right]`.
#
# Exemplul 1
#   Input:
#     operations = ["NumArray","sumRange","sumRange","sumRange"]
#     arguments = [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
#   Output: [null,1,-1,-3]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁴`
#   - `-10⁵ ≤ nums[i] ≤ 10⁵`
#   - `0 ≤ left ≤ right < len(nums)`
#   - Cel mult 10⁴ apeluri către `sumRange`
#
# Teste:  python3 test.py 303      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):


    def sumRange(self, left: int, right: int) -> int:
        
# @lc code=end
