def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        # target - valoarea de la indexul i
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []


print(two_sum([3, 8, 4, 11, 6, 7], 10))

arr = [3, 8, 4]
print(len(arr))
print("\n")
arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i])
print("\n", arr2)

print("\n", range(len(arr)))
