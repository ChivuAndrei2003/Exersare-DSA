#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# Medium  ·  Trie
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
# Proiectează o structură de date în care poți adăuga cuvinte și apoi verifica dacă un string se
# potrivește cu vreun cuvânt adăugat.
#
# Implementează clasa `WordDictionary`. `WordDictionary()` creează obiectul. `addWord(word)`
# adaugă `word` în structură. `search(word)` returnează `True` dacă vreun cuvânt adăugat se
# potrivește cu `word` și `False` altfel; în `search`, `word` poate conține puncte, iar un `.` se
# potrivește cu orice literă.
#
# Exemplul 1
#   Input:
#     operations = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#     arguments = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#   Output: [null,null,null,null,false,true,true,true]
#
# Notă: Primul element din `operations` construiește obiectul, restul sunt apeluri de metode cu
# argumentele din `arguments`. Output-ul are `null` pentru constructor și metodele fără valoare.
#
# Constrângeri:
#   - `1 ≤ len(word) ≤ 25`
#   - În `addWord`, `word` conține doar litere mici ale alfabetului englez
#   - În `search`, `word` conține litere mici și `.`
#   - Un `word` căutat are cel mult 2 puncte
#   - Cel mult 10⁴ apeluri către `addWord` și `search`
#
# Teste:  python3 test.py 211      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class WordDictionary:

    def __init__(self):


    def addWord(self, word: str) -> None:


    def search(self, word: str) -> bool:
        
# @lc code=end
