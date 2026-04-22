class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the two separate segments
        l = 0
        r = len(nums)-1
        mid = (l + r)//2
        #if rotated
        while l <= r:
            mid = (l + r)//2
            #cannot use target to abstract direction only the exit condition
            #if middle greater than left and right necessarily the case that left side is the sorted side
            #can see if target lies in between if not look from middle to right to find another sorted side
            if nums[mid]==target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            #right side is sorted
            else:
                if nums[mid]< target <= nums[r]:
                    l = mid  +1
                else:
                    r = mid -1
        return -1



