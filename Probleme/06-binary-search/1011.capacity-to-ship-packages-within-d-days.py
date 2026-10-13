#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
# Medium  ·  Binary Search
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
#
# Pachetele de pe o bandă trebuie transportate cu o navă în cel mult `days` zile. Pachetul `i` are
# greutatea `weights[i]`.
#
# În fiecare zi nava se încarcă cu pachete în ordinea de pe bandă (ordinea din `weights`), fără să
# depășească capacitatea ei maximă.
#
# Returnează cea mai mică capacitate a navei cu care toate pachetele ajung la destinație în cel
# mult `days` zile.
#
# Exemplul 1
#   Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
#   Output: 15
#
# Exemplul 2
#   Input:  weights = [3,2,2,4,1,4], days = 3
#   Output: 6
#
# Exemplul 3
#   Input:  weights = [1,2,3,1,1], days = 4
#   Output: 3
#
# Constrângeri:
#   - `1 ≤ days ≤ len(weights) ≤ 5 · 10⁴`
#   - `1 ≤ weights[i] ≤ 500`
#
# Teste:  python3 test.py 1011      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
# @lc code=end
