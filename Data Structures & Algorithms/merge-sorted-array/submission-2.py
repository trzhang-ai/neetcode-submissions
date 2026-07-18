class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        nums1[:] = nums1[:m]
        while i < len(nums1) and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
        nums1.extend(nums2[j:])
        
        