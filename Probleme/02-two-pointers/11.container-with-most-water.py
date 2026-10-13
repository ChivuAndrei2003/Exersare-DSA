#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# Medium  ·  Two Pointers
# https://leetcode.com/problems/container-with-most-water/
#
# Primești un array `height` de lungime n. La fiecare poziție `i` se află o linie verticală cu
# capetele în `(i, 0)` și `(i, height[i])`.
#
# Alege două linii care, împreună cu axa x, formează recipientul în care încape cea mai multă apă
# și returnează acea cantitate. Recipientul nu poate fi înclinat: apa urcă până la linia mai
# scurtă, deci aria e `min(height[i], height[j]) · (j − i)`.
#
# Exemplul 1
#   Input:  height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#
# Exemplul 2
#   Input:  height = [1,1]
#   Output: 1
#
# Constrângeri:
#   - `n == len(height)`
#   - `2 ≤ n ≤ 10⁵`
#   - `0 ≤ height[i] ≤ 10⁴`
#
# Teste:  python3 test.py 11      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
# @lc code=end
