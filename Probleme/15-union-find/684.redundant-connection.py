#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# Medium  ·  Union-Find (DSU)
# https://leetcode.com/problems/redundant-connection/
#
# Un arbore e un graf neorientat conex și fără cicluri. Primești un graf care a pornit ca un
# arbore cu `n` noduri, numerotate de la 1 la `n`, la care s-a adăugat o muchie în plus, între
# două noduri diferite, care nu exista deja. Graful e dat ca `edges`, un array de lungime `n`, cu
# `edges[i] = [a, b]`.
#
# Returnează o muchie care poate fi eliminată astfel încât graful rămas să fie un arbore cu `n`
# noduri. Dacă sunt mai multe răspunsuri, returnează muchia care apare ultima în `edges`.
#
# Exemplul 1
#   Input:  edges = [[1,2],[1,3],[2,3]]
#   Output: [2,3]
#
# Exemplul 2
#   Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
#   Output: [1,4]
#
# Constrângeri:
#   - `n == len(edges)`
#   - `3 ≤ n ≤ 1000`
#   - `len(edges[i]) == 2`
#   - `1 ≤ a < b ≤ n`
#   - Fără muchii repetate
#   - Graful e conex
#
# Teste:  python3 test.py 684      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
# @lc code=end
