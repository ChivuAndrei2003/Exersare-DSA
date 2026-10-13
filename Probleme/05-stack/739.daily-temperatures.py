#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# Medium  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/daily-temperatures/
#
# Primești un array `temperatures` cu temperaturile zilnice. Returnează un array `answer` în care
# `answer[i]` e numărul de zile pe care trebuie să le aștepți, după ziua `i`, până la o
# temperatură mai mare. Dacă nu urmează nicio zi mai caldă, `answer[i] = 0`.
#
# Exemplul 1
#   Input:  temperatures = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
#
# Exemplul 2
#   Input:  temperatures = [30,40,50,60]
#   Output: [1,1,1,0]
#
# Exemplul 3
#   Input:  temperatures = [30,60,90]
#   Output: [1,1,0]
#
# Constrângeri:
#   - `1 ≤ len(temperatures) ≤ 10⁵`
#   - `30 ≤ temperatures[i] ≤ 100`
#
# Teste:  python3 test.py 739      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
# @lc code=end
