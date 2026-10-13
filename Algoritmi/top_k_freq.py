from collections import Counter


def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]  # index = frecvență
    for num, c in count.items():
        buckets[c].append(num)
    res = []
    for c in range(len(buckets) - 1, 0, -1):
        for num in buckets[c]:
            res.append(num)
            if len(res) == k:
                return res
    return res
