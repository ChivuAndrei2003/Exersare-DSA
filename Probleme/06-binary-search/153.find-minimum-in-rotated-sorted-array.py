#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# Medium  ·  Binary Search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Un array de lungime n, sortat crescător și cu elemente distincte, a fost rotit de 1 până la n
# ori (o rotire mută ultimul element pe prima poziție). De exemplu, `[0, 1, 2, 4, 5, 6, 7]` devine
# `[4, 5, 6, 7, 0, 1, 2]` după 4 rotiri și rămâne neschimbat după 7.
#
# Primești array-ul rotit, `nums`. Returnează elementul minim, cu un algoritm O(log n).
#
# Exemplul 1
#   Input:  nums = [3,4,5,1,2]
#   Output: 1
#
# Exemplul 2
#   Input:  nums = [4,5,6,7,0,1,2]
#   Output: 0
#
# Exemplul 3
#   Input:  nums = [11,13,15,17]
#   Output: 11
#
# Constrângeri:
#   - `n == len(nums)`
#   - `1 ≤ n ≤ 5000`
#   - `-5000 ≤ nums[i] ≤ 5000`
#   - Toate valorile din `nums` sunt distincte
#   - `nums` e sortat și rotit de 1 până la n ori
#
# Teste:  python3 test.py 153      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
# @lc code=end
