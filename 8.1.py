class Solution(object):
    def subsetXORSum(self, nums):
        def subsets(nums, index, xor_sum):
            if index == len(nums):
                return xor_sum
            return subsets(nums, index + 1, xor_sum ^ nums[index]) + subsets(nums, index + 1, xor_sum)
        return subsets(nums, 0, 0)

nums = [1, 3]
nums_2 = [5, 1, 6]
nums_3 = [3, 4, 5, 6, 7, 8]
solution = Solution()
print(solution.subsetXORSum(nums))
print(solution.subsetXORSum(nums_2))
print(solution.subsetXORSum(nums_3))


