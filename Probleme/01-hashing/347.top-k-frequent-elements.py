#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# Medium  ·  Arrays & Hashing
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Primești un array de întregi `nums` și un întreg `k`. Returnează cele mai frecvente `k`
# elemente, în orice ordine.
#
# Follow-up: algoritmul trebuie să fie mai rapid decât O(n log n), unde n e lungimea array-ului.
#
# Exemplul 1
#   Input:  nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
#
# Exemplul 2
#   Input:  nums = [1], k = 1
#   Output: [1]
#
# Exemplul 3
#   Input:  nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#   Output: [1,2]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `1 ≤ len(nums) ≤ 10⁵`
#   - `-10⁴ ≤ nums[i] ≤ 10⁴`
#   - `1 ≤ k ≤` numărul de valori distincte din `nums`
#   - Răspunsul e unic
#
# Teste:  python3 test.py 347      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # type: ignore

        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]  # len +1 bcs index=freq

        # append the frequencies to buckets
        for num, c in count.items():
            buckets[c].append(num)
            
        res = []
        for c in range(len(buckets) - 1, 0, -1):
            for num in buckets[c]:
                res.append(num)
                if len(res) == k:
                    return res
        return res


# @lc code=end
# 1 2 3 4
