class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = {}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in left:
                left[i]+=1
            else:
                left[i] = 1
        for i in t:
            if i in left:
                if left[i]>0:
                    left[i]-=1
                else:
                    return False
            else:
                return False
        return True