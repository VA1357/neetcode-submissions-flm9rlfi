class Solution:
    def trap(self, height: List[int]) -> int:
        #find how much water can be stored at each column by subtracting local max (min of left anf right bars at a current position) with the amount of bars in given column
        #perhaps need to assign a left and right bar at any given column and use that to calculate?
        #solution to above question is we can do one right pass and one left pass
        #these track max seen so far, and the minimum of these shows which is the limiting bar height for storing water
        seenmaxl = -1
        seenmaxr = -1
        #find curr water level that can be held with min(height[l], height[r])-height[i] for a given index i
        leftpass = [0]*len(height)
        rightpass = [0]*len(height)

        ans = 0
        for i in range(len(height)):
            if height[i] > seenmaxl:
                seenmaxl = height[i]
            else:
                leftpass[i] = seenmaxl-height[i]
        for i in range(len(height)-1,-1,-1):
            if height[i] > seenmaxr:
                seenmaxr = height[i]
            else:
                rightpass[i] = seenmaxr-height[i]
        print(leftpass)
        print(rightpass)
        for i in range(len(height)):
            ans += min(rightpass[i], leftpass[i])
        return ans