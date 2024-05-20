def min_weight_difference(N, weights):
    def helper(index, pile1_weight, pile2_weight):
        if index == N:
            return abs(pile1_weight - pile2_weight)
        diff1 = helper(index + 1, pile1_weight + weights[index], pile2_weight)
        diff2 = helper(index + 1, pile1_weight, pile2_weight + weights[index])
        return min(diff1, diff2)
    return helper(0, 0, 0)

N = 5
weights = [3, 1, 4, 2, 2]
print(min_weight_difference(N, weights))

#Correct!
