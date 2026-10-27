# Fereastră de mărime fixă
def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window

    for r in range(k, len(nums)):
        window += nums[r] - nums[r - k]
        best = max(best, window)
    return window


print(max_sum_k([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  # prints 24

# Fereastră de mărime variabilă


# Fereastră variabilă: cel mai lung substring fără repetiții
def length_of_longest_substring(s):
    seen = set()
    l = best = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        best = max(best, r - l + 1)
    return best


print("***")
print(length_of_longest_substring("abbaaacadn"))


# Fereastră variabilă — cea mai lungă validă
def longest_without_repeat(s):
    count = {}
    l = best = 0

    for r, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1  # 1.extinde
        while count[ch] > 1:  # 2. cât timp e invalidă, strânge
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)  # actualizeaza raspunsul
    return best, count.items()  # count items l-am pus eu , NU-I NEVOIE de el


print(
    "\n", longest_without_repeat("abracadabra")
)  # AFISEAZA : (4, dict_items([('a', 1), ('b', 1), ('r', 1), ('c', 0), ('d', 0)]))


# Fereastră variabilă — cea mai scurtă validă
def min_subarray_len(target, nums):
    l = total = 0
    best = float("inf")

    for r, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if best == float("inf") else best

print("\n", min_subarray_len(6, [1,2,3,4,5,6,])) # prints 1
