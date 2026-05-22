class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #save state of chars in a dictionary
        #replacement happens to all instances of a char
        i = 0
        j = 1
        state = [0]*26
        if not s:
            return 0
        uniq = 1
        state[ord(s[0])-ord('A')] +=1
        output = 0
        while j < len(s):
            state[ord(s[j])-ord('A')]+=1
            uniq = max(uniq, state[ord(s[j])-ord('A')])

            if (j-i+1)-(uniq) > k:
                while (j-i+1)-(uniq) > k:
                    state[ord(s[i]) - ord('A')]-=1
                    i+=1
            j+=1

        return j-i