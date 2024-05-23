def min_flip_count(A):
    total_sum = sum(A)
    half_sum = total_sum // 2
    n = len(A)

    dp = [[False] * (half_sum + 1) for _ in range(n + 1)]
    flips = [[float('inf')] * (half_sum + 1) for _ in range(n + 1)]

    dp[0][0] = True
    flips[0][0] = 0

    for i in range(1, n + 1):
        for j in range(half_sum + 1):
            dp[i][j] = dp[i - 1][j]
            flips[i][j] = flips[i - 1][j]
            if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:
                dp[i][j] = True
                flips[i][j] = min(flips[i][j], flips[i - 1][j - A[i - 1]] + 1)

    for j in range(half_sum, -1, -1):
        if dp[n][j]:
            best_sum = j
            break

    min_non_negative_sum = total_sum - 2 * best_sum
    min_flips = flips[n][best_sum]
    return min_flips

A1 = [15, 10, 6]
A2 = [14, 10, 4]
print(min_flip_count(A1))
print(min_flip_count(A2))
