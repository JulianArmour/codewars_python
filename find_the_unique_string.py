# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

from itertools import combinations


def find_uniq(arr):
    # arr[:3] contains at least two similar character entries and at most 1 different. Thus two entries are guaranteed
    # to have similar characters (Pigeonhole Principle). Here we check each combination of two entries until we find
    # that match.
    for charset1, charset2 in combinations((set(entry.lower()) for entry in arr[:3]), 2):
        if charset1 == charset2:
            similar = charset1
            break

    for entry in arr:
        if set(entry.lower()) != similar:
            return entry


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
