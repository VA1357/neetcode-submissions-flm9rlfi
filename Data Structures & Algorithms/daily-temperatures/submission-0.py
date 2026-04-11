class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        maxi = -1
        ans = [0]*len(temperatures)
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                oldindex = stack.pop()
                ans[oldindex] = idx - oldindex
            stack.append(idx)
        return ans