class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        sta = 100000
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                sta = min(prices[i], sta)
            if sta != 100000 and prices[i] > prices[i+1]:
                ans += prices[i] - sta
                sta = 100000
        if sta != 100000:
            ans += prices[len(prices) - 1] - sta
        return ans
# O(n)