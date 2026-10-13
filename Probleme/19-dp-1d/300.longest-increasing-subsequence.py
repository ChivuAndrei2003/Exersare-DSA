#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# Medium  ·  Dynamic Programming — 1D
# https://leetcode.com/problems/longest-increasing-subsequence/
#
# Primești un array de întregi `nums`. Returnează lungimea celui mai lung subșir strict crescător.
#
# Un subșir se obține ștergând zero sau mai multe elemente, fără a schimba ordinea celor rămase
# (elementele nu trebuie să fie vecine). Follow-up: găsește un algoritm în O(n log n).
#
# Exemplul 1
#   Input:  nums = [10,9,2,5,3,7,101,18]
#   Output: 4
#
# Exemplul 2
#   Input:  nums = [0,1,0,3,2,3]
#   Output: 4
#
# Exemplul 3
#   Input:  nums = [7,7,7,7,7,7,7]
#   Output: 1
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 2500`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#
# Teste:  python3 test.py 300      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
# @lc code=end
