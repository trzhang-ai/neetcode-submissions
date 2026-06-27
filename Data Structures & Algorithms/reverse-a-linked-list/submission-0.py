# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        nodes = [ListNode(val) for val in vals[::-1]]
        i = 0
        while not nodes[i].next:
            if i + 1 == len(nodes):
                break
            nodes[i].next = nodes[i + 1]
            i += 1
        return nodes[0]
