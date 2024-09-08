# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if list contains only one node
        if (head.next == None):
            return True

        # dividing list into two sublists

        slow, fast, prev = head, head, None
        while (fast != None and fast.next != None):

            prev = slow
            slow = slow.next
            fast = fast.next.next

        # first list
        first = head
        prev.next = None

        # second list
        second = slow

        # reverse the second list
        prev = None
        while (second != None):

            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev

        # compare the two lists
        while (first != None):

            if (first.val != second.val):
                return False

            first = first.next
            second = second.next

        return True