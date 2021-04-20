#산것보다 비싸면 바로 판다
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = -1
        for i in range(len(prices) - 1):
            if buy < 0 and prices[i] < prices[i + 1]:
                buy = prices[i]
            elif prices[i] > prices[i + 1] and buy >= 0:
                ans += prices[i] - buy
                buy = -1

        if buy >= 0 and prices[-1] > buy:
            ans += prices[-1] - buy
        return ans

