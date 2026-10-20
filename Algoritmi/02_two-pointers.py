"""
  ****** PE SCURT ******

* Pointeri opuși (l la început, r la final):
   pe array sortat sau când e clar ce capăt muți. Fiecare pas elimină un element → O(n) în loc de O(n²).
* Aceeași direcție (read / write): unul citește, celălalt arată unde scrii următorul element valid.
   Pentru modificări in-place (duplicate, zerouri).
* K-Sum (3Sum, 4Sum): sortezi, fixezi un element cu o buclă și rezolvi restul cu two pointers.
"""


## Pointeri opuși pe un array sortat
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        s = nums[l] + nums[r]

        if s == target:
            return [l, r]
        if s < target:
            l += 1  # am nevoie de o sumă mai mare

        if s > target:
            r -= 1  # am nevoie de o sumă mai mica
    return []


print(two_sum_sorted([1, 3, 4, 6, 8, 11, 14], 17))  # [1,6]


# A doua formă: read / write în aceeași direcție : elimină duplicatele in-place
"""
    r citește fiecare element,
    w arată unde scriem următorul element unic. Tot ce e la stânga lui w e rezultatul final.
||
  *  Același șablon rezolvă Move Zeroes, Remove Element, Remove Duplicates, comprimarea unui șir.
  *  Pointerul de scriere nu-l depășește pe cel de citire, deci nu suprascrii nimic necitit.
"""


def remove_duplciates(nums):
    w = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[w - 1]:
            nums[w] = nums[r]
            w += 1
    return w


print("\n")
print(remove_duplciates([1, 1, 2, 3, 5, 5]))  # afiseaza : 4


# 3Sum: sortare + fixare + two pointers
def three_sum(nums):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l += 1
            if s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res
