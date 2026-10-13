#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# Medium  ·  Greedy
# https://leetcode.com/problems/jump-game-ii/
#
# Primești un array de întregi `nums` de lungime n. Pornești de pe indexul 0. Fiecare `nums[i]` e
# lungimea maximă a unui salt înainte de pe indexul `i`: poți sări pe orice `i + j`, cu `0 ≤ j ≤
# nums[i]` și `i + j < n`.
#
# Returnează numărul minim de salturi cu care ajungi pe ultimul index. Testele garantează că se
# poate ajunge acolo.
#
# Exemplul 1
#   Input:  nums = [2,3,1,1,4]
#   Output: 2
#
# Exemplul 2
#   Input:  nums = [2,3,0,1,4]
#   Output: 2
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁴`
#   - `0 ≤ nums[i] ≤ 1000`
#   - Se poate ajunge mereu la ultimul index
#
# Teste:  python3 test.py 45      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        
# @lc code=end
