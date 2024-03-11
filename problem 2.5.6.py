class Solution:
    def solve(self, A):
        n = len(A)
        result = [0] * n
        left, right = 0, n - 1
        idx = n - 1
        
        while left <= right:
            left_square = A[left] * A[left]
            right_square = A[right] * A[right]
            
            if left_square > right_square:
                result[idx] = left_square
                left += 1
            else:
                result[idx] = right_square
                right -= 1
            idx -= 1
        
        return result
        
#Abdelrahman Mohamed 11/314a