class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for i in strs:
            alphabet = [0]*26
            for j in i:
               alphabet[ord(j)-ord('a')] +=1
            if tuple(alphabet) in counts:
                counts[tuple(alphabet)].append(i)
            else:
                counts[tuple(alphabet)] = [i]
        ans = []
        for i in counts:
            ans.append(counts[i])
        return ans
            