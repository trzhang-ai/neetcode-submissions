class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counters = []
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counters.append(counter)
                counter = 0
        else:
            counters.append(counter)
        max_count = max(counters)
        return max_count