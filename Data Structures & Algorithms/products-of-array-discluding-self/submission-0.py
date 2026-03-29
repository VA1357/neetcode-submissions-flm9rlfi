class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        prefix[0] = 1
        prefix[1] = nums[0]
        suffix[len(nums)-1] = 1
        suffix[len(nums)-2] = nums[len(nums)-1]
        for i in range(2,len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            print(suffix[i+1])
            suffix[i] = nums[i+1] * suffix[i+1]
        
        return [a*b for a, b in zip(prefix, suffix)]
       


       
        
