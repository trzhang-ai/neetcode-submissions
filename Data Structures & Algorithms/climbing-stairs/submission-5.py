class Solution:

    def climbStairs(self, n: int) -> int:

        memo = {}

        def climb(k: int) -> int:
            if k <= 2:
                return k
            elif k in memo:
                return memo[k]
            else:
                memo[k] = climb(k - 1) + climb(k - 2)
                return memo[k]
        
        return climb(n)
    

        