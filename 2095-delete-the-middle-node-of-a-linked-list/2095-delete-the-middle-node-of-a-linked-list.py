# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Traverse the list to count the total number of nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        # Step 2: Calculate the middle index
        middle_index = count // 2
        
        # Step 3: If the list has only one node, return None
        if count == 1:
            return None
        
        # Step 4: Traverse again to reach the node just before the middle node
        temp = head
        for _ in range(middle_index - 1):
            temp = temp.next
        
        # Step 5: Remove the middle node by adjusting the pointers
        temp.next = temp.next.next
        
        return head