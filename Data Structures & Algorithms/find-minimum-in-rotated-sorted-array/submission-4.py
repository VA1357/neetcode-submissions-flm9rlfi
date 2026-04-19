class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search where left and right bounds represent the number of rotations rather than the values?
        #actually values are useful if num[0] greater than num[len(num)-1] we know it has been rotated at least once
        #perhaps this could be used to show that search space needs to only be removed from the left?
        #need to find the end of the increasing behavior
        #if mid value greater than r value discard mid (+ 1 it)
        l, r = 0, len(nums)-1
        mid = 0
        while l<r:
            #guess how far it was rotated between 1 and n times
            mid =(l+r)//2
            print(nums[mid])
            print(nums[l])
            print(nums[r])
            if nums[l]<nums[r]:
                return nums[l]
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]

