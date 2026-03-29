class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        while nums:
            curr = nums.pop(0)
            if target - curr in nums:
                return [count, nums.index(target-curr)+count+1]
            count+=1
        return []


