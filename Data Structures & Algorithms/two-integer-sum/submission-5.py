class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for idx, val in enumerate(nums):
            if target-val in count:
                return [count[target-val][0], idx]
            else:
                count[val]=(idx,target-val)
        return False
        