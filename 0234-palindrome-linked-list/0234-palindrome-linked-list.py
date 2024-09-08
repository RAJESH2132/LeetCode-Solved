# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Reverse list up to midpoint using fast/slow pointers
        fast, slow = head, head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # Handle case when list is odd length
        if fast:
            slow = slow.next

        # Compare reversed left half with right half
        while rev and slow:
            if rev.val != slow.val:
                return False
            rev, slow = rev.next, slow.next

        return True