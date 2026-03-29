class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_dicts = defaultdict(list)
        for i in strs:
            dict = [0]*26
            for c in i:
                dict[ord(c)-97]+=1
            total_dicts[tuple(dict)].append(i)
        return list(total_dicts.values())
            





        