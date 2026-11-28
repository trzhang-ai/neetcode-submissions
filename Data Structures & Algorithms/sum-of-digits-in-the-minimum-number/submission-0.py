class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        smallest = min(nums)
        smallest = sum([int(i) for i in list(str(smallest))])
        print(smallest)
        if smallest % 2:
            return 0
        else:
            return 1
