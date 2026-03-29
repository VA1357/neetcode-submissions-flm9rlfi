class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = {}

        for i,n in enumerate(nums):
            if n in lis:
                return [lis[n],i]
            lis[target-n] = i
        return [0,0]