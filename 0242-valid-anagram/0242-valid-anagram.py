class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. sort it and see if it's the same string!
        # s_res = ''.join(sorted(s))
        # t_res = ''.join(sorted(t))
        # if s_res == t_res:
        #     return True
        # return False

        # 2. iterate through s & t, build frequency map and see if it differs
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for j in t:
            # check if j is in freq. if not, FALSE
            if j in freq:
                freq[j]-=1
            else:
                return False
        
        for i in freq:
            if freq[i] != 0:
                return False
        return True