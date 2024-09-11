# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        values.sort()
        current = head
        for value in values:
            current.val = value
            current = current.next
        
        return head