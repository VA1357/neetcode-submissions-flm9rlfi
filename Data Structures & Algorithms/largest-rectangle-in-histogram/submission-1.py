class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            
        #first idea: each number can have 3 cases:
        #1. it itself is the constraint of the largest rectangle (single long rectangle)
        #2. it is constrained by a number right of it
        #3. it is constrained by a number left of it
        #how to find constraints, maybe two pass one from each side?
        #left pass example:
        #for i = 0, value is 7. for every consecutive number if it is lower, constrain by right, which is 1
        #cannot exit until a value greater than 1 is found as 7 could still be further constrained otherwise
        #above sentence is wrong and where mistake is, need to look at which rectangle each value makes instead
        # so for first 7 see right constraint is 1, for 1 right constraint is itself it cant get to 7, and for second 7 see there is no right constraint (set to 4 as last element of array)
        #so find first smaller bar on right and left per value
        n = len(heights)

        # left[i] = index of first smaller bar to the left of i
        # if none exists, use -1
        left = [-1] * n

        # right[i] = index of first smaller bar to the right of i
        # if none exists, use n
        right = [n] * n

        stack = []

        # build left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # build right
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            ans = max(ans, heights[i] * width)

        return ans

       