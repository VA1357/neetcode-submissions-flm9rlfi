class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for counts in strs:
            ans += str(len(counts)) + "#" + counts
        return ans 
    def decode(self, s: str) -> List[str]:
        ans = []
        end = 0
        i = 0
        while i < len(s):
            j = s.find("#",i)
            print(j)
            limit = int(s[i:j])
            ans.append(s[j+1:j+1+limit])
            i = j + limit + 1

        return ans