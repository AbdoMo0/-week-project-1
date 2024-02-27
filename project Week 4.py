# Abdelrahman Mohamed 11/314a
class Solution:
    def threeSumClosest(self, A, B):
        A.sort()
        closest_sum = float('inf')
        
        for i in range(len(A) - 2):
            left = i + 1 
            right = len(A) - 1
            while left < right:
                curr_sum = A[i] + A[left] + A[right]
                if abs(B - curr_sum) < abs(B - closest_sum):
                    closest_sum = curr_sum
                if curr_sum > B:
                    right -= 1
                elif curr_sum < B:
                    left += 1
                else:
                    return closest_sum
        return closest_sum

solution = Solution()
print(solution.threeSumClosest([-1, 2, 1, -4], 1))
print(solution.threeSumClosest([1, 2, 3], 6)) 
