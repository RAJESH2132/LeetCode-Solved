def rotation(self,nums,start,end):
    n = len(nums)
    while start<=end:
        nums[start],nums[end] = nums[end], nums[start]
        start+=1
        end -= 1
    return nums    
class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        rotation(self,nums,0,n-k-1)
        rotation(self,nums,n-k,n-1)
        rotation(self,nums,0,n-1)
        