# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # Move the fastp pointer N nodes ahead
        for _ in range(n):
            fast = fast.next

        # If fastp becomes None, the Nth node from the end is the head
        if fast is None:
            return head.next

        # Move both pointers until fastp reaches the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Delete the Nth node from the end
        slow.next = slow.next.next
        return head