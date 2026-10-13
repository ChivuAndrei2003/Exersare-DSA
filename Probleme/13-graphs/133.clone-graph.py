#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# Medium  ·  Graphs — BFS / DFS
# https://leetcode.com/problems/clone-graph/
#
# Primești o referință la un nod dintr-un graf neorientat și conex. Returnează o copie profundă
# (clonă) a grafului.
#
# Fiecare nod are o valoare întreagă `val` și o listă `neighbors` cu vecinii lui. Valoarea unui
# nod coincide cu numărul lui: primul nod are `val = 1`, al doilea `val = 2` și așa mai departe.
#
# Copia trebuie să fie formată din noduri noi, cu aceleași valori și aceleași legături. Pentru un
# graf gol returnezi `None`.
#
# Exemplul 1
#   Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
#   Output: [[2,4],[1,3],[2,4],[1,3]]
#
# Exemplul 2
#   Input:  adjList = [[]]
#   Output: [[]]
#
# Exemplul 3
#   Input:  adjList = []
#   Output: []
#
# Notă: Graful e dat ca listă de adiacență (nodul `i + 1` are vecinii `adjList[i]`). Funcția ta
# primește nodul 1.
#
# Constrângeri:
#   - Numărul de noduri e în intervalul `[0, 100]`
#   - `1 ≤ Node.val ≤ 100`
#   - `Node.val` e unic pentru fiecare nod
#   - Graful nu are muchii repetate și nici bucle (muchii de la un nod la el însuși)
#   - Graful e conex: toate nodurile sunt accesibile din nodul primit
#
# Teste:  python3 test.py 133      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
# @lc code=end
