class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            if num not in hashMap:
                if target - num in hashMap:
                    return [hashMap[target - num], i]
                hashMap[num] = i
            else:
                if (target - num) in hashMap:
                    return [hashMap[num], i]
