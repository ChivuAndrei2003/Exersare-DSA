#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
# Easy  ·  Heap / Top K
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#
# Proiectează o clasă care găsește al `k`-lea cel mai mare element dintr-un flux de numere. E
# vorba de al `k`-lea în ordine sortată (duplicatele se numără), nu de al `k`-lea element
# distinct.
#
# Implementează clasa `KthLargest`: `KthLargest(k, nums)` primește întregul `k` și valorile
# inițiale ale fluxului, iar `add(val)` adaugă `val` în flux și returnează al `k`-lea cel mai mare
# element de până acum.
#
# Exemplul 1
#   Input:
#     operations = ["KthLargest","add","add","add","add","add"]
#     arguments = [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
#   Output: [null,4,5,5,8,8]
#
# Exemplul 2
#   Input:
#     operations = ["KthLargest","add","add","add","add"]
#     arguments = [[4,[7,7,7,7,8,3]],[2],[10],[9],[9]]
#   Output: [null,7,7,7,8]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `0 ≤ len(nums) ≤ 10⁴`
#   - `1 ≤ k ≤ len(nums) + 1`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#   - `-10⁴ ≤ val ≤ 10⁴`
#   - Cel mult 10⁴ apeluri către `add`
#
# Teste:  python3 test.py 703      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):


    def add(self, val: int) -> int:
        
# @lc code=end
