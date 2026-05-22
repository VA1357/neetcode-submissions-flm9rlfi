class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #find each char in s1 in s2 until you find the left most one
        #can do this with two pointers that shrink until you see a s1 character
        if len(s1)>len(s2):
            return False
        s3 = [0] * 26
        s4 = [0] * 26

        for i in s1:
            s3[ord(i)-ord('a')] +=1
        
        k = 0
        l = len(s1)-1
        for i in s2[k:l+1]:
            s4[ord(i)-ord('a')] +=1
        while l < len(s2):
            if s4 == s3:
                return True
            s4[ord(s2[k])-ord('a')]-=1
            k +=1
            l +=1
            if l < len(s2):
                s4[ord(s2[l])-ord('a')]+=1
            else:
                break
        return False

