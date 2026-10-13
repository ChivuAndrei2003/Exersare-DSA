def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        # target - valoarea de la indexul i
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


print(two_sum([3, 8, 4, 11, 6, 7], 10))
