from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        print(count)
        ans = count.most_common(k)
        return [answer[0] for answer in ans]