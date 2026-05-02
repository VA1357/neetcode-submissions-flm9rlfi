import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = 0
        r = len(nums1)
        total = len(nums1) + len(nums2)
        isodd = total %2

        if not nums1:
            if isodd:
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2 - 1] + nums2[(len(nums2)//2)]) / 2
        elif not nums2:
            if isodd:
                return nums1[len(nums1)//2]
            else:
                return (nums1[len(nums1)//2 - 1] + nums1[(len(nums1)//2)]) / 2
        while l <= r:
            #assert left partition value
            mid = (l + r) //2
            #calculate right partition value
            rmid = (total + 1)//2 - mid
            #for current parititon to be correct:
            #either partition is at end of array or value to the right of both partitions is bigger
            #this is trivial if comparing within array but not if comparing across array
            #need to find left partition value such that the following:
            #left side max from nums1 < right side min from nums2
            #left side max from nums 2 < right side min from nums1
            if mid==0:
                leftmax1 = -1 * math.inf
            else:
                leftmax1 = nums1[mid-1]
            if mid == len(nums1):
                rightmin1 = math.inf
            else:
                rightmin1 = nums1[mid]
            if rmid == 0:
                leftmax2 = -1 * math.inf
            else:
                leftmax2 = nums2[rmid-1]
            if rmid == len(nums2):
                rightmin2 = math.inf
            else:
                rightmin2 = nums2[rmid]
            if max(leftmax1, leftmax2) <= min(rightmin1, rightmin2):
                if isodd:
                    return max(leftmax1,leftmax2)
                else:
                    return (max(leftmax1, leftmax2) + min(rightmin1, rightmin2))/2
            else:
                if rightmin2 < leftmax1:
                    r = mid - 1
                else:
                    l = mid + 1