#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#
# Medium  ·  Heap / Top K
# https://leetcode.com/problems/task-scheduler/
#
# Primești un array `tasks` cu sarcinile pe care trebuie să le execute un procesor, fiecare notată
# cu o literă de la A la Z, și un întreg `n`. Fiecare interval de timp e ocupat de o sarcină sau e
# liber (idle). Sarcinile pot fi executate în orice ordine.
#
# Restricție: între două execuții ale aceleiași sarcini trebuie să treacă cel puțin `n` intervale.
#
# Returnează numărul minim de intervale în care procesorul termină toate sarcinile.
#
# Exemplul 1
#   Input:  tasks = ["A","A","A","B","B","B"], n = 2
#   Output: 8
#
# Exemplul 2
#   Input:  tasks = ["A","C","A","B","D","B"], n = 1
#   Output: 6
#
# Exemplul 3
#   Input:  tasks = ["A","A","A","B","B","B"], n = 3
#   Output: 10
#
# Constrângeri:
#   - `1 ≤ len(tasks) ≤ 10⁴`
#   - `tasks[i]` e o literă mare a alfabetului englez
#   - `0 ≤ n ≤ 100`
#
# Teste:  python3 test.py 621      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
# @lc code=end
