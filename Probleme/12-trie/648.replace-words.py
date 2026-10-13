#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# Medium  ·  Trie
# https://leetcode.com/problems/replace-words/
#
# În engleză, o rădăcină poate fi urmată de alte litere ca să formeze un cuvânt mai lung, un
# derivat: din rădăcina „help” se obține derivatul „helpful”.
#
# Primești un dicționar de rădăcini, `dictionary`, și o propoziție `sentence`, cu cuvintele
# separate prin câte un spațiu. Înlocuiește fiecare derivat din propoziție cu rădăcina din care se
# formează. Dacă un cuvânt se poate forma din mai multe rădăcini, alege-o pe cea mai scurtă.
# Cuvintele care nu încep cu nicio rădăcină rămân neschimbate.
#
# Returnează propoziția de după înlocuire.
#
# Exemplul 1
#   Input:  dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
#   Output: "the cat was rat by the bat"
#
# Exemplul 2
#   Input:  dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
#   Output: "a a b c"
#
# Constrângeri:
#   - `1 ≤ len(dictionary) ≤ 1000`
#   - `1 ≤ len(dictionary[i]) ≤ 100`
#   - `dictionary[i]` conține doar litere mici
#   - `1 ≤ len(sentence) ≤ 10⁶`
#   - `sentence` conține doar litere mici și spații
#   - `sentence` are între 1 și 1000 de cuvinte, fiecare de lungime 1–1000
#   - Cuvintele sunt separate prin exact un spațiu, fără spații la început sau la sfârșit
#
# Teste:  python3 test.py 648      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
# @lc code=end
