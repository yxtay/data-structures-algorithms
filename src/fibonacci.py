def fib_rec(n):
    if n <= 1:
        return n  # base cases: return 0 or 1 if n is 0 or 1, respectively
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a
