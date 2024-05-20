from itertools import permutations

def count_permutations_with_beautiful_points(n, k):
    count = 0
    for perm in permutations(range(1, n + 1)):
        beautiful_points = sum(1 for i in range(n) if perm[i] == i + 1)
        if beautiful_points == k:
            count += 1
    return count

n, k = map(int, input().split())
print(count_permutations_with_beautiful_points(n, k))

#you are not able to use import permutations
