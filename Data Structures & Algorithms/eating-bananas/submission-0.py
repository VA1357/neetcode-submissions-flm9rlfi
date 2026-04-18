import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #constraint is the h value, so binary search left is 1 and right is h
        #another constraint is that you cant just sum and divide due to the pile intervals not carrying over
        #find how long a pile takes with ceil(pile[i]/k) where k is the rate we need to find
        #right bound is max value of piles (each pile takes 1 hour then)
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for i in piles:
                count += (math.ceil(i/mid)) 
            if count > h:
                l = mid + 1
            else:
                r = mid - 1
        return l

