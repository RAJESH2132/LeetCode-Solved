# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize dummy node which simplifies edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Skip the desired node
        second.next = second.next.next
        
        return dummy.next