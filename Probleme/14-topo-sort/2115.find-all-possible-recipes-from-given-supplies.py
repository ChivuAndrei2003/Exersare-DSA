#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#
# Medium  ·  Topological Sort
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
#
# Ai informații despre `n` rețete: `recipes[i]` e numele rețetei `i`, iar `ingredients[i]` e lista
# ingredientelor de care are nevoie. O rețetă poate fi ingredient pentru altă rețetă, adică
# `ingredients[i]` poate conține nume din `recipes`.
#
# Primești și `supplies`, ingredientele pe care le ai de la început, în cantitate nelimitată. Poți
# găti o rețetă dacă ai toate ingredientele ei, din stoc sau gătite de tine.
#
# Returnează lista tuturor rețetelor pe care le poți găti, în orice ordine. Două rețete se pot
# conține reciproc ca ingrediente — caz în care niciuna nu poate fi gătită.
#
# Exemplul 1
#   Input:
#     recipes = ["bread"]
#     ingredients = [["yeast","flour"]]
#     supplies = ["yeast","flour","corn"]
#   Output: ["bread"]
#
# Exemplul 2
#   Input:
#     recipes = ["bread","sandwich"]
#     ingredients = [["yeast","flour"],["bread","meat"]]
#     supplies = ["yeast","flour","meat"]
#   Output: ["bread","sandwich"]
#
# Exemplul 3
#   Input:
#     recipes = ["bread","sandwich","burger"]
#     ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
#     supplies = ["yeast","flour","meat"]
#   Output: ["bread","sandwich","burger"]
#
# Notă: Ordinea elementelor din răspuns nu contează.
#
# Constrângeri:
#   - `n == len(recipes) == len(ingredients)`
#   - `1 ≤ n ≤ 100`
#   - `1 ≤ len(ingredients[i]), len(supplies) ≤ 100`
#   - Fiecare nume (rețetă, ingredient, stoc) are între 1 și 10 litere mici ale alfabetului
#     englez
#   - Toate valorile din `recipes` și `supplies`, luate împreună, sunt distincte
#   - `ingredients[i]` nu conține duplicate
#
# Teste:  python3 test.py 2115      (în VS Code: Cmd+Shift+B)
#
from dsa import *  # ce are LeetCode deja importat: List, Optional, ListNode, TreeNode, Counter, deque, heappush...

# @lc code=start
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
# @lc code=end
