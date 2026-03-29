class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for i in strs:
            alphabet = [0]*26
            for j in i:
                alphabet[ord(j)-ord('a')] +=1
            idx = tuple(alphabet)
            if idx in counts:
                counts[idx].append(i)
            else:
                counts[idx] = [i]
        return [i for i in counts.values()]