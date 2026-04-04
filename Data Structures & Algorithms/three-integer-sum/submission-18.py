class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use sorted two sum solution to find sums of 2, and use a single loop to find the 3rd value thus giving you sum of 3
        #avoiding duplicates is hard part, make sure whenever a number is considered to add, you skip if its the same as last number since array sorted
        nums.sort()
        res = []
        for idx, val in enumerate(nums):
            if val>0:
                break
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
                elif l + r > -val:
                    j-=1
                elif l + r < -val:
                    i+=1
        return res
                
