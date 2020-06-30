def fib_rec(n):
    if n <= 1:
        return n  # base cases: return 0 or 1 if n is 0 or 1, respectively
    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_rec_memo(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}

    if n in memo:
        return memo[n]
    else:
        result = fib_rec_memo(n - 1, memo) + fib_rec_memo(n - 2, memo)
        memo[n] = result
        return result


def fib_dp(n):
    dp = [0, 1]
    for _ in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]


def fib_dp_op(n):
    dp = [0, 1]
    if n == 0:
        return dp[0]
    for _ in range(1, n):
        current = dp[0] + dp[1]
        dp[0] = dp[1]
        dp[1] = current
    return dp[-1]


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a
