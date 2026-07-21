class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = [num for row in matrix for num in row]
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] < target:
                low = mid + 1
            elif array[mid] > target:
                high = mid - 1
            else:
                return True
        return False

        
        