def find_next(triplets):
    for triplet in triplets:
        if triplet and all(triplet[0] not in trip[1:] for trip in triplets if len(trip) > 1):
            return triplet[0]


def prune_next(next_char, triplets):
    for triplet in triplets:
        if triplet and triplet[0] is next_char:
            triplet.pop(0)


def recoverSecret(triplets):
    secret = []
    while True:
        next_char = find_next(triplets)
        if next_char is None:
            return "".join(secret)
        secret.append(next_char)
        prune_next(next_char, triplets)


triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(recoverSecret(triplets))
