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
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, reslen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if reslen != float("infinity") else ""


# @lc code=end
