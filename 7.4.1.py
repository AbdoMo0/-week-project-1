class Solution:
    def searchRange(self, A, B):
        def searchLeft(A, target):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == target:
                    if mid == 0 or A[mid - 1] < target:
                        return mid
                    else:
                        right = mid - 1
                elif A[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        def searchRight(A, target):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == target:
                    if mid == len(A) - 1 or A[mid + 1] > target:
                        return mid
                    else:
                        left = mid + 1
                elif A[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        left_index = searchLeft(A, B)
        if left_index == -1:
            return [-1, -1]
        right_index = searchRight(A, B)
        return [left_index, right_index]

solution = Solution()
A1 = [5, 7, 7, 8, 8, 10]
B1 = 8
print(solution.searchRange(A1, B1))
A2 = [5, 17, 100, 111]
B2 = 3
print(solution.searchRange(A2, B2))