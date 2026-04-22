class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(target, l,r,arr):
            if not arr or r < l:
                return -1
            mid = (l + r)//2
            if arr[mid]==target:
                return mid
            if arr[mid] < target:
                return binary(target,mid + 1, r,arr)
            else:
                return binary(target,l,mid -1,arr)
            return -1

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
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target <= nums[mid]:
                    return binary(target,l,mid,nums)
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    return binary(target,mid,r,nums)
                else:
                    r = mid -1
        return -1



