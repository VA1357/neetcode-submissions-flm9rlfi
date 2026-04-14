class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #only put indices in the binary search function
        #always make a new function for binary search recursion
        def binary(left: int, right: int) -> int:
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(left, mid - 1)
            else:
                return binary(mid + 1, right)

        return binary(0, len(nums) - 1)