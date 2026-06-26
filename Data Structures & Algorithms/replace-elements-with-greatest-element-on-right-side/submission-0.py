class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
            i += 1
        return arr
        