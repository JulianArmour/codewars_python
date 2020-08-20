def snail(snail_map):
    result = []
    while len(snail_map) != 0:
        result.extend(snail_map.pop(0))
        snail_map = list(reversed(list(zip(*snail_map))))
    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(snail(array))
