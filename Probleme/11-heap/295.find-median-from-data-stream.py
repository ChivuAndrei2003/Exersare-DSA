#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# Hard  ·  Heap / Top K
# https://leetcode.com/problems/find-median-from-data-stream/
#
# Mediana e valoarea din mijlocul unei liste sortate de întregi; dacă lista are un număr par de
# elemente, mediana e media celor două valori din mijloc.
#
# Implementează clasa `MedianFinder`: `MedianFinder()` creează obiectul, `addNum(num)` adaugă
# întregul `num` din fluxul de date, iar `findMedian()` returnează mediana tuturor elementelor
# adăugate până atunci.
#
# Follow-up: cum optimizezi dacă toate numerele sunt în intervalul `[0, 100]`? Dar dacă 99% dintre
# ele sunt?
#
# Exemplul 1
#   Input:
#     operations = ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
#     arguments = [[],[1],[2],[],[3],[]]
#   Output: [null,null,null,1.5,null,2]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Notă: Răspunsurile se acceptă cu o eroare de până la 10⁻⁵.
#
# Constrângeri:
#   - `-10⁵ ≤ num ≤ 10⁵`
#   - `findMedian` e apelat doar când structura are cel puțin un element
#   - Cel mult 5 · 10⁴ apeluri către `addNum` și `findMedian`
#
# Teste:  python3 test.py 295      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class MedianFinder:

    def __init__(self):


    def addNum(self, num: int) -> None:


    def findMedian(self) -> float:
        
# @lc code=end
