class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        n = len(a)
        low = 1
        high = n-2
        if n == 1:
            return a[0]
        if a[0] != a[1]:
            return a[0]
        if a[n-1]!=a[n-2]:
            return a[n-1]
        
        while low <= high:
            mid = (low+high)//2
            if a[mid]!=a[mid-1] and a[mid]!=a[mid+1]:
                return a[mid]
            if ((mid%2==0 and a[mid]==a[mid+1]) or (mid%2==1 and a[mid]==a[mid-1])):
                low = mid+1
            else:
                high = mid-1
        return -1