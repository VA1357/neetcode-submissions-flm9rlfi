class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        if not prices:
            return 0
        ans = 0
        while j < len(prices) and i < j:
            if prices[i] > prices[j]:
                i = j
            else:
                ans = max(ans, prices[j] - prices[i])
            j+=1
        return ans