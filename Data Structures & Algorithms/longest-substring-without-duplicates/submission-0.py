from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        alpha = defaultdict(int)
        i = 0
        j = 1
        output = 1

        alpha[s[0]] = 1

        while j < len(s):
            if alpha[s[j]] == 0:
                alpha[s[j]] += 1
                j += 1
            else:
                while s[i] != s[j]:
                    alpha[s[i]] -= 1
                    i += 1

                alpha[s[i]] -= 1
                i+=1

            output = max(output, j - i)

        return output