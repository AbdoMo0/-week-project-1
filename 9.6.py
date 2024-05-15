class Solution:
    def numDecodings(self, A):
        MOD = 10**9 + 7
        n = len(A)
        if n == 0 or A[0] =='0':
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if A[i-1] != '0':
                dp[i] += dp[i-1]
            if A[i-2] == '1' or (A[i-2] == '2' and A[i-1] <= '6'):
                dp[i] += dp[i-2]
            dp[i] %= MOD
        return dp[n]
solution = Solution()
A1 = "8"
A2 = "12"
print(solution.numDecodings(A1))
print(solution.numDecodings(A2))