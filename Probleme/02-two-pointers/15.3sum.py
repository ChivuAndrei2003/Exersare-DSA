#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# Medium  ·  Two Pointers
# https://leetcode.com/problems/3sum/
#
# Primești un array de întregi `nums`. Returnează toate tripletele `[nums[i], nums[j], nums[k]]`
# cu indici diferiți doi câte doi (`i ≠ j`, `i ≠ k`, `j ≠ k`) și cu suma 0.
#
# Rezultatul nu trebuie să conțină triplete duplicate: aceleași trei valori apar o singură dată.
# Ordinea tripletelor și a valorilor din ele nu contează.
#
# Exemplul 1
#   Input:  nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
#
# Exemplul 2
#   Input:  nums = [0,1,1]
#   Output: []
#
# Exemplul 3
#   Input:  nums = [0,0,0]
#   Output: [[0,0,0]]
#
# Notă: Ordinea nu contează (nici în listă, nici în interiorul grupurilor).
#
# Constrângeri:
#   - `3 ≤ len(nums) ≤ 3000`
#   - `-10⁵ ≤ nums[i] ≤ 10⁵`
#
# Teste:  python3 test.py 15      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  # type: ignore
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

        return res


# @lc code=end
