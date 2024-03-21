def kthFactor(self, n, k):
        divisors, sqrt_n = [], int(n**0.5)
        for x in range(1, sqrt_n+1):
            if n % x == 0:
                k-=1
                divisors.append(x)
                if k == 0:
                    return x

        # 1 2 3 4 6 12
        # 1 2 4
        if (sqrt_n * sqrt_n == n):
            k += 1
            
        if k <= len(divisors):
            return n / divisors[len(divisors) - k]
        else:
            return -1 