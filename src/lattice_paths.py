def num_paths_rec(height, width):
    if height == 0 or width == 0:
        return 1
    return num_paths_rec(height, width - 1) + num_paths_rec(height - 1, width)


def num_paths_dp(height, width):
    memo = [[1] * (width + 1) for _ in range(0, height + 1)]
    for i, row in enumerate(memo):
        for j, _ in enumerate(row):
            if i == 0 or j == 0:
                continue
            memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    return memo[-1][-1]


def num_paths_dp_2(height, width):
    row = [1] * (width + 1)
    for _ in range(1, height + 1):
        for j in range(1, width + 1):
            row[j] += row[j - 1]
    return row[-1]
