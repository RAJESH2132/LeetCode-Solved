# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        
        # 步驟 1: 使用快慢指針找到相遇點
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # 沒有環
        
        # 步驟 2: 找到環的起始點
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow