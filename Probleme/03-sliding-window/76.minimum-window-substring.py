#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# Hard  ·  Sliding Window
# https://leetcode.com/problems/minimum-window-substring/
#
# Primești două stringuri, `s` (de lungime m) și `t` (de lungime n). Returnează cel mai scurt
# substring al lui `s` care conține toate caracterele din `t`, inclusiv duplicatele: dacă o literă
# apare de două ori în `t`, trebuie să apară de cel puțin două ori în fereastră. Dacă nu există un
# astfel de substring, returnează stringul gol `""`.
#
# Literele mari și cele mici sunt caractere diferite. Follow-up: găsește un algoritm în O(m + n).
#
# Exemplul 1
#   Input:  s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"
#
# Exemplul 2
#   Input:  s = "a", t = "a"
#   Output: "a"
#
# Exemplul 3
#   Input:  s = "a", t = "aa"
#   Output: ""
#
# Notă: Dacă sunt mai multe ferestre minime, oricare e acceptată.
#
# Constrângeri:
#   - `m == len(s)`, `n == len(t)`
#   - `1 ≤ m, n ≤ 10⁵`
#   - `s` și `t` conțin litere mari și mici ale alfabetului englez
#
# Teste:  python3 test.py 76      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
# @lc code=end
