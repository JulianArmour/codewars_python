def fib_gen():
    cur_fib, next_fib = 1, 1
    while True:
        yield cur_fib
        cur_fib, next_fib = next_fib, cur_fib + next_fib


def perimeter(n):
    length_sum = 0
    fib_generator = fib_gen()
    for _ in range(n + 1):
        length_sum += next(fib_generator)
    return 4 * length_sum
