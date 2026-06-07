class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s1 = [0] * 52
        #need one way to store all unique chars in s and t
        s2 = [0] * 52
        need = 0
        for i in t:
            if s1[ord(i)-ord('a')] ==0:
                need+=1
                #print(f'{ord(i)-ord('a')}')
            s1[ord(i)-ord('a')] +=1
        
        have = 0
        ans = ""
        lenans = 10001
        i = 0
        j = 0
        #print(f's1: {s1}')
        while j < len(s):
            
            #if in t then add to s2
            s2[ord(s[j])-ord('a')]+=1
            if (s2[ord(s[j])-ord('a')]> 0) and s2[ord(s[j])-ord('a')] == s1[ord(s[j])-ord('a')]:
            #if the total count matches for s2 and s1 than append have
                have+=1
            #if have = need then log the current substring/length, append i until have is less than need then continue appending j
            #print(f'{ord(s[j])-ord('a')}: {s2}')
            
            while have == need and i <=j:
                if (j-i+1) < lenans:
                        ans = s[i:j+1]
                        lenans = (j-i+1)
                    
                print(f'have: {have}, need: {need}')
                print(s[i])

                s2[ord(s[i])-ord('a')]-=1
                
               
                if s2[ord(s[i])-ord('a')] < s1[ord(s[i])-ord('a')]:
                    have-=1
                i+=1
            j+=1
        return ans



            
            