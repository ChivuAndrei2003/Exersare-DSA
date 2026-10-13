#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# Easy  ·  Bit Manipulation
# https://leetcode.com/problems/counting-bits/
#
# Primești un întreg `n`. Returnează un array `ans` de lungime `n + 1` în care, pentru fiecare `i`
# cu `0 ≤ i ≤ n`, `ans[i]` e numărul de biți de 1 din reprezentarea binară a lui `i`.
#
# Follow-up: soluția O(n log n) e la îndemână; poți rezolva în O(n), într-o singură trecere?
#
# Exemplul 1
#   Input:  n = 2
#   Output: [0,1,1]
#
# Exemplul 2
#   Input:  n = 5
#   Output: [0,1,1,2,1,2]
#
# Constrângeri:
#   - `0 ≤ n ≤ 10⁵`
#
# Teste:  python3 test.py 338      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        
# @lc code=end
