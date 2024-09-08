# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        # Initialize pointers
        odd = head
        even = head.next
        even_head = even

        # Traverse the list
        while even and even.next:
            odd.next = even.next  # Link odd nodes
            odd = odd.next        # Move odd pointer

            even.next = odd.next  # Link even nodes
            even = even.next      # Move even pointer

        # Join the even list at the end of the odd list
        odd.next = even_head

        return head
