class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lproduct = [0]*len(nums)
        lproduct[0] = nums[0]
        rproduct = [0]*len(nums)
        rproduct[-1] = nums[-1]
        for i in range(1,len(nums)):
            lproduct[i] = lproduct[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            rproduct[i] = rproduct[i+1] * nums[i]
        print(lproduct)
        print(rproduct)
        res = [0]*len(lproduct)
        res[-1] = lproduct[-2]
        res[0] = rproduct[1]
        print(res)
        for i in range(1,len(nums)-1):
            res[i] = lproduct[i-1] * rproduct[i+1]
        return res
