from functools import cache

class Solution:

    def climbStairs(self, n: int) -> int:

        @cache
        def climb(k: int) -> int:
            if k <= 2:
                return k
            else:
                return climb(k - 1) + climb(k - 2)

        return climb(n)
            

        