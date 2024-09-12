# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse both linked lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        # Step 2: Add the numbers
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Step 3: Reverse the result to get the final answer in the correct order
        return self.reverseList(dummy_head.next)