def beauty(arr):
    mini=float('inf')
    maxi=float('-inf')

    for i in range(26):
        if arr[i] > 0:
            mini = min(mini,arr[i])
        
        maxi=max(maxi,arr[i])
    
    return maxi-mini

class Solution:
    def beautySum(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            freq=[0] * 26
            for j in range(i,n):
                freq[ord(s[j])-97]+=1
                ans+=beauty(freq)

        return ans


        