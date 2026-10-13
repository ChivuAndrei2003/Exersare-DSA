#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# Medium  ·  Stack & Monotonic Stack
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# Primești `tokens`, o expresie aritmetică în notație poloneză inversă (postfixată): operanzii vin
# înaintea operatorului. Evaluează expresia și returnează rezultatul, un întreg.
#
# Operatorii valizi sunt `+`, `-`, `*` și `/`; fiecare operand e un întreg sau rezultatul altei
# expresii. Împărțirea a doi întregi trunchiază spre zero (în Python: `int(a / b)`, nu `a // b`).
#
# Expresia e mereu validă, nu apare împărțire la zero, iar rezultatul și toate calculele
# intermediare încap pe 32 de biți.
#
# Exemplul 1
#   Input:  tokens = ["2","1","+","3","*"]
#   Output: 9
#
# Exemplul 2
#   Input:  tokens = ["4","13","5","/","+"]
#   Output: 6
#
# Exemplul 3
#   Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#   Output: 22
#
# Constrângeri:
#   - `1 ≤ len(tokens) ≤ 10⁴`
#   - `tokens[i]` e un operator (`+`, `-`, `*`, `/`) sau un întreg din intervalul `[-200,
#     200]`
#
# Teste:  python3 test.py 150      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
# @lc code=end
