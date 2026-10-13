#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#
# Medium  ·  Shortest Path (Dijkstra)
# https://leetcode.com/problems/path-with-maximum-probability/
#
# Ai un graf neorientat ponderat cu `n` noduri, numerotate de la 0, dat prin lista de muchii
# `edges`: `edges[i] = [a, b]` e o muchie între `a` și `b`, iar `succProb[i]` e probabilitatea de
# a o traversa cu succes.
#
# Primești două noduri, `start_node` și `end_node`. Găsește drumul cu probabilitatea maximă de
# succes dintre ele (produsul probabilităților muchiilor) și returnează acea probabilitate. Dacă
# nu există niciun drum, returnează 0.
#
# Răspunsul e acceptat dacă diferă de cel corect cu cel mult 10⁻⁵.
#
# Exemplul 1
#   Input:
#     n = 3
#     edges = [[0,1],[1,2],[0,2]]
#     succProb = [0.5,0.5,0.2]
#     start_node = 0
#     end_node = 2
#   Output: 0.25
#
# Exemplul 2
#   Input:
#     n = 3
#     edges = [[0,1],[1,2],[0,2]]
#     succProb = [0.5,0.5,0.3]
#     start_node = 0
#     end_node = 2
#   Output: 0.3
#
# Exemplul 3
#   Input:  n = 3, edges = [[0,1]], succProb = [0.5], start_node = 0, end_node = 2
#   Output: 0
#
# Notă: Răspunsurile se acceptă cu o eroare de până la 10⁻⁵.
#
# Constrângeri:
#   - `2 ≤ n ≤ 10⁴`
#   - `0 ≤ start_node, end_node < n`
#   - `start_node ≠ end_node`
#   - `0 ≤ a, b < n`
#   - `a ≠ b`
#   - `0 ≤ len(succProb) == len(edges) ≤ 2 · 10⁴`
#   - `0 ≤ succProb[i] ≤ 1`
#   - Între două noduri există cel mult o muchie
#
# Teste:  python3 test.py 1514      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
# @lc code=end
