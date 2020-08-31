from bisect import bisect


def hamming(n):
    numbers = [1]
    for ham_no in range(n - 1):
        ham = numbers[ham_no]
        for h in [ham * 2, ham * 3, ham * 5]:
            insert_index = bisect(numbers, h)
            # only insert if h isn't already in `numbers`
            if numbers[insert_index - 1] != h:
                numbers.insert(insert_index, h)
    return numbers[n - 1]


for i in range(5):
    print(hamming(i + 1), end=" ")
