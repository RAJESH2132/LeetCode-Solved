class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n-1
        ans = float("inf")

        while low <= high:
            mid = low + (high-low)//2

            if arr[low] <= arr[high]:
                ans = min(ans,arr[low])
                break
            if arr[low] <= arr[mid]:
                ans = min(ans,arr[low])
                low = mid+1
            else:
                ans = min(ans,arr[mid])
                high = mid-1
        return ans