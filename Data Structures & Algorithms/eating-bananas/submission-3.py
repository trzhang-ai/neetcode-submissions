import math
class Solution:

    def eatingPerPile(self, bananas, rate):
        time = bananas / rate
        time = math.ceil(time)
        return time

    def eatingAllBananas(self, piles, rate):
        total_time = 0
        for p in piles:
            total_time += self.eatingPerPile(p, rate)
        return total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate, max_rate = 1, max(piles)
        while min_rate <= max_rate:
            rate = (min_rate + max_rate) // 2
            total_time = self.eatingAllBananas(piles, rate)
            if total_time > h:
                min_rate = rate + 1
            else:
                if rate - 1 > 0 and self.eatingAllBananas(piles, rate - 1) > h:
                    return rate
                max_rate = rate - 1
        return min_rate
        