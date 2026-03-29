class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in lis:
                return [lis[diff], i]
            lis[n] = i
        return []


