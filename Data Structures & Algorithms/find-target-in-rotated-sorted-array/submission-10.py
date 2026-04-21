class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search start from ends of the array
        #due to ascending nature we can look at current mid
        #if curr value less than target move to the right
        #else move left
        [2, 0, -1, 5, 4, 3]

        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            leftSum = abs(target-nums[l])
            rightSum = abs(target-nums[l])
            print(nums[mid])
            if target-nums[mid]==0:
                return mid
            if leftSum == 0:
                return l
            if rightSum == 0:
                return r
            if leftSum < rightSum:
                if abs(target-nums[mid]) < rightSum:
                    r = mid - 1
                else:
                    r-=1
            else:
                if abs(target-nums[mid]) > rightSum:
                    l = mid + 1
                else:
                    l+=1
        return -1