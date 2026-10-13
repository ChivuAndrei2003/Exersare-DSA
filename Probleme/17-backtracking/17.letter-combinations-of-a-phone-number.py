#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# Medium  ·  Backtracking
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Primești un string `digits` cu cifre de la 2 la 9. Returnează toate combinațiile de litere pe
# care le poate reprezenta, în orice ordine. Pentru un string gol, răspunsul e lista goală.
#
# Corespondența dintre cifre și litere e cea de pe tastatura unui telefon cu butoane: 2 → abc, 3 →
# def, 4 → ghi, 5 → jkl, 6 → mno, 7 → pqrs, 8 → tuv, 9 → wxyz.
#
# Exemplul 1
#   Input:  digits = "23"
#   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Exemplul 2
#   Input:  digits = ""
#   Output: []
#
# Exemplul 3
#   Input:  digits = "2"
#   Output: ["a","b","c"]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `0 ≤ len(digits) ≤ 4` (pe LeetCode, cel puțin o cifră)
#   - `digits[i]` e o cifră din intervalul `2`–`9`
#
# Teste:  python3 test.py 17      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
# @lc code=end
