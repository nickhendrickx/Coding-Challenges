def climbStairs(self, n: int) -> int:
        
        memo = [0,1]

        for i in range(1, n+1):
            temp = memo[0] + memo[1]
            memo[0] = memo[1]
            memo[1] = temp

        return memo[1]