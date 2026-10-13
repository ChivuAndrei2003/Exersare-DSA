#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# Medium  ·  Arrays & Hashing
# https://leetcode.com/problems/group-anagrams/
#
# Primești o listă de stringuri, `strs`. Grupează anagramele: două cuvinte ajung în același grup
# dacă unul se obține din celălalt prin rearanjarea literelor.
#
# Grupurile și cuvintele din ele pot fi returnate în orice ordine.
#
# Exemplul 1
#   Input:  strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Exemplul 2
#   Input:  strs = [""]
#   Output: [[""]]
#
# Exemplul 3
#   Input:  strs = ["a"]
#   Output: [["a"]]
#
# Notă: Ordinea nu contează (nici în listă, nici în interiorul grupurilor).
#
# Constrângeri:
#   - `1 ≤ len(strs) ≤ 10⁴`
#   - `0 ≤ len(strs[i]) ≤ 100`
#   - `strs[i]` conține doar litere mici ale alfabetului englez
#
# Teste:  python3 test.py 49      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # type: ignore
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())


# @lc code=end
