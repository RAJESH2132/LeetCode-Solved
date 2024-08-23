class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = 0
        negative = 1
        arr = [0]*n
        for num in nums:
            if num > 0:
                arr[positive] = num
                positive += 2
            else:
                arr[negative] = num
                negative += 2
        return arr
