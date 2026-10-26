#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# Hard  ·  Two Pointers
# https://leetcode.com/problems/trapping-rain-water/
#
# Primești `height`, un array de n întregi nenegativi care descrie un relief: fiecare element e
# înălțimea unei bare de lățime 1.
#
# Calculează câte unități de apă rămân prinse între bare după ploaie.
#
# Exemplul 1 1 2 1 1
#   Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6
#
# Exemplul 2
#   Input:  height = [4,2,0,3,2,5]
#   Output: 9
#
# Constrângeri:
#   - `n == len(height)`
#   - `1 ≤ n ≤ 2 · 10⁴`
#   - `0 ≤ height[i] ≤ 10⁵`
#
# Teste:  python3 test.py 42      (în VS Code: Cmd+Shift+B)
#


from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:  # type: ignore
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        total = 0

        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
        return total


# @lc code=end
