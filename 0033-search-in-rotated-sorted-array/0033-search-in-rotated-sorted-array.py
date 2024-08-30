class Solution:
    def search(self, arr: List[int], k: int) -> int:
        low = 0 
        n = len(arr)
        high = n-1
        while low <= high:
            mid = (low+high)//2

            if arr[mid] == k:
                return mid 
            if arr[low] <= arr[mid]:
                if arr[low] <=k and arr[mid]>=k:
                    high = mid-1
                else:
                    low = mid +1
            else:  # if right part is sorted
                if arr[mid] <= k and k <= arr[high]:
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1
        return -1