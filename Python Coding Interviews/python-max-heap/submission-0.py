import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    output = []
    neg_nums = [-num for num in nums]
    heapq.heapify(neg_nums)
    while neg_nums:
        output.append(-heapq.heappop(neg_nums))
    return output





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
