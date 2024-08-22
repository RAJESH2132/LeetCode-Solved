class Solution:
    def sortColors(self, arr: List[int]) -> None:
        n = len(arr)
        low, mid = 0,0
        high = n-1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low+=1
                mid+=1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        