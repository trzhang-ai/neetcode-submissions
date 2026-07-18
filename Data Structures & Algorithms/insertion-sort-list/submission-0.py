# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        for i in range(1, len(vals)):
            j = i - 1
            while j >= 0 and vals[j] > vals[j + 1]:
                tmp = vals[j + 1]
                vals[j + 1] = vals[j]
                vals[j] = tmp
                j -= 1

        head = ListNode(vals[0])
        current = head

        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return head        