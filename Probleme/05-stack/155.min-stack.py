#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# Medium  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/min-stack/
#
# Proiectează o stivă care, pe lângă operațiile obișnuite, returnează elementul minim în timp
# constant.
#
# Implementează clasa `MinStack`: `push(val)` pune `val` pe stivă, `pop()` scoate elementul din
# vârf, `top()` returnează elementul din vârf, iar `getMin()` returnează cel mai mic element din
# stivă. Toate operațiile trebuie să ruleze în O(1).
#
# Exemplul 1
#   Input:
#     operations = ["MinStack","push","push","push","getMin","pop","top","getMin"]
#     arguments = [[],[-2],[0],[-3],[],[],[],[]]
#   Output: [null,null,null,null,-3,null,0,-2]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `-2³¹ ≤ val ≤ 2³¹ − 1`
#   - `pop`, `top` și `getMin` sunt apelate doar pe stive nevide
#   - Cel mult 3 · 10⁴ apeluri în total
#
# Teste:  python3 test.py 155      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class MinStack:

    def __init__(self):


    def push(self, val: int) -> None:


    def pop(self) -> None:


    def top(self) -> int:


    def getMin(self) -> int:
        
# @lc code=end
