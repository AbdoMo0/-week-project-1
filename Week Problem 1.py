# Abdelrahman Mohamed 11/314a
class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def primesum(self, A):
        for i in range(2, A // 2 + 1):
            if self.is_prime(i) and self.is_prime(A - i):
                if i == A - i: 
                    return [i, i]
                else:
                    return [i, A - i]
