class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Compute the next greater element for each element in nums2
        next_greater_map = {}
        stack = []
        
        for num in nums2:
            # Pop all elements from the stack that are smaller than the current num
            while stack and stack[-1] < num:
                next_greater_map[stack.pop()] = num
            # Push the current element to the stack
            stack.append(num)
        
        # Elements left in stack have no next greater element, map them to -1
        while stack:
            next_greater_map[stack.pop()] = -1
        
        # Step 2: Answer the queries for each element in nums1 using the map
        return [next_greater_map[num] for num in nums1]