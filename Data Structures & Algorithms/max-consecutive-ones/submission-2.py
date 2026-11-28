class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        i = 0
        streaks = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            if count > streaks:
                streaks = count
            i += 1
        return streaks
        