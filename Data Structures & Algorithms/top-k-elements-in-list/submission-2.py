from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #KEY: you do not need to fix max first then set bucket list length. Since the highest frequency possible is len(nums), you set length to len(nums) + 1
        buckets = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            #count frequency of each num and store it in a dict
            count[i] = 1 + count.get(i, 0)
        #take the counted frequencies and place in buckets
        for num, freqs in count.items():
            buckets[freqs].append(num)
        ans = []
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans
        return []