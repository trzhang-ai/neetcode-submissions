class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        min_num = min(nums)
        max_num = max(nums)
        counts = [0] * (max_num - min_num + 1)
        for num in nums:
            counts[range(min_num, max_num + 1).index(num)] += 1
        nums[:] = []
        for cnt, r in zip(counts, range(min_num, max_num + 1)):
            nums.extend([r] * cnt)
        