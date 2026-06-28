# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vals1, vals2 = [], []
        while list1:
            vals1.append(list1.val)
            list1 = list1.next
        while list2:
            vals2.append(list2.val)
            list2 = list2.next
        vals = vals1 + vals2
        if len(vals) == 0:
            return None
        vals.sort()
        nodes = [ListNode(val=val) for val in vals]
        i = 0
        while i < len(nodes):
            if i + 1 == len(nodes):
                break
            nodes[i].next = nodes[i + 1]
            i += 1
        return nodes[0]






                        