from collections import defaultdict


# grupare dupa o cheie
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # semnătura grupului
        groups[key].append(s)
    return list(groups.values())

