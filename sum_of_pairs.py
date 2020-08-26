def sum_pairs(ints, s):
    seen = set()
    for n in ints:
        matching = s - n
        if matching in seen:
            return [matching, n]
        seen.add(n)
    return None
