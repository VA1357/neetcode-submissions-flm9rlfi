class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, val in enumerate(nums):
            if idx>0 and val==nums[idx-1]:
                continue
            i = idx + 1
            j = len(nums)-1
            while i < j:
                l = nums[i]
                r = nums[j]
                if l + r==-val:
                    res.append([val, l, r])
                    while i<j and nums[i]==l:
                        i+=1
                    while j>i and nums[j]==r: 
                        j-=1
                elif val + l + r > 0:
                    j-=1
                elif val + l + r < 0:
                    i+=1
        return res
                
