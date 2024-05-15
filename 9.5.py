class Solution:
    def wordBreak(self, A, B):
        word_set = set(B)
        n = len(A)
        memo = [-1] * n
        def canSegment(start):
            if start == n:
                return True
            if memo[start] != -1:
                return memo[start]
            for end in range(start + 1, n + 1):
                if A[start:end] in word_set and canSegment(end):
                    memo[start] = 1
                    return True
                memo[start] = 0
            return False
        return int(canSegment(0))
solution = Solution()
A1 = "myinterviewtrainer"
B1 = ["trainer", "my", "interview"]
A2 = "a"
B2 = ["aaa"]
print(solution.wordBreak(A1, B1))  # Output: 1
print(solution.wordBreak(A2, B2))  # Output: 0