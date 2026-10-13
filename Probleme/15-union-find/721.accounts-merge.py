#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# Medium  ·  Union-Find (DSU)
# https://leetcode.com/problems/accounts-merge/
#
# Primești o listă de conturi, `accounts`. În fiecare `accounts[i]`, primul element e numele
# titularului, iar restul sunt adresele de email ale contului.
#
# Două conturi aparțin aceleiași persoane dacă au cel puțin un email comun. Atenție: două conturi
# cu același nume pot fi ale unor persoane diferite (numele se pot repeta), dar toate conturile
# unei persoane au același nume.
#
# Unește conturile aceleiași persoane și returnează-le în formatul: primul element e numele, iar
# restul sunt emailurile, sortate și fără duplicate. Conturile pot fi returnate în orice ordine.
#
# Exemplul 1
#   Input:
#     accounts = [
#       ["John","johnsmith@mail.com","john_newyork@mail.com"],
#       ["John","johnsmith@mail.com","john00@mail.com"],
#       ["Mary","mary@mail.com"],
#       ["John","johnnybravo@mail.com"]
#     ]
#   Output: [
#     ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#     ["Mary","mary@mail.com"],
#     ["John","johnnybravo@mail.com"]
#   ]
#
# Exemplul 2
#   Input:
#     accounts = [
#       ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
#       ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
#       ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
#       ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
#       ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
#     ]
#   Output: [
#     ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
#     ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
#     ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
#     ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
#     ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
#   ]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ len(accounts) ≤ 1000`
#   - `2 ≤ len(accounts[i]) ≤ 10`
#   - `1 ≤ len(accounts[i][j]) ≤ 30`
#   - `accounts[i][0]` conține doar litere ale alfabetului englez
#   - `accounts[i][j]`, pentru `j > 0`, e o adresă de email validă
#
# Teste:  python3 test.py 721      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
# @lc code=end
