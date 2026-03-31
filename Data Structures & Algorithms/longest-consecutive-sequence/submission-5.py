class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #repeats create extra work so remove at start
        nums = set(nums)
        starts = []
        #start each sequence with numbers that dont have any before them, then use set O(1) lookups and brute force
        for i in nums:
            if i-1 not in nums:
                starts.append(i)
        res = 0
        #brute force, for each sequence count manually using O(1) lookups
        for i in starts:
            count = 1
            val = i
            while val+1 in nums:
                val +=1
                count+=1
            res = max(res, count)
        return res