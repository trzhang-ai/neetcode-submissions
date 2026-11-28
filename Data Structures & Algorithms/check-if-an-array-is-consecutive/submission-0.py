class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        x, n = min(nums), len(nums)
        return set(nums) == set(range(x, x + n))