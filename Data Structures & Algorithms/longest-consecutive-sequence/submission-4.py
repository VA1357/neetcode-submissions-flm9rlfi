class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #repeats create extra work so remove at start
        nums = set(nums)
        starts = []
        vals = []
        for i in nums:
            if i-1 not in nums:
                starts.append(i)
            else:
                vals.append(i)
        res = 0
        for i in starts:
            count = 1
            val = i
            while val+1 in nums:
                val +=1
                count+=1
            res = max(res, count)
        return res