#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# Medium  ·  Greedy
# https://leetcode.com/problems/gas-station/
#
# Pe un traseu circular sunt `n` benzinării; la benzinăria `i` găsești `gas[i]` unități de
# combustibil. Mașina ta are rezervor nelimitat și consumă `cost[i]` unități ca să ajungă de la
# benzinăria `i` la următoarea, `i + 1`. Pornești cu rezervorul gol, de la una dintre benzinării.
#
# Returnează indexul benzinăriei de la care poți face un tur complet, în sensul acelor de
# ceasornic, sau −1 dacă nu se poate.
#
# Exemplul 1
#   Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
#   Output: 3
#
# Exemplul 2
#   Input:  gas = [2,3,4], cost = [3,4,3]
#   Output: -1
#
# Exemplul 3
#   Input:  gas = [5,1,2,3,4], cost = [4,4,1,5,1]
#   Output: 4
#
# Notă: Orice stație de start validă e acceptată.
#
# Constrângeri:
#   - `n == len(gas) == len(cost)`
#   - `1 ≤ n ≤ 10⁵`
#   - `0 ≤ gas[i], cost[i] ≤ 10⁴`
#   - Pe LeetCode, dacă există un răspuns, el e unic
#
# Teste:  python3 test.py 134      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
# @lc code=end
