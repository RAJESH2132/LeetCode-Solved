class Solution:
    def binarySearch(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1  # Base case

        # Perform the steps:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        return self.binarySearch(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)