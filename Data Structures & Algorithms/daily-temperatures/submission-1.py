class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #as usual for array problem see if order of comparison matters if question has to do with max
        #since the max can only be to the right we can make a stack of current seen numbers
        #everytime we consider a number we remove any n-1 numbers if they are lower
        #logic is that if the current value is greater than a previous temp we can immediately resolve value for old temp index, we dont need to see more numbers. 
        #Any older temps greater than current value live in the stack until their counterpart is found
        stack = []
        ans = [0]*len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                oldindex = stack.pop()
                ans[oldindex] = idx - oldindex
            stack.append(idx)
        return ans