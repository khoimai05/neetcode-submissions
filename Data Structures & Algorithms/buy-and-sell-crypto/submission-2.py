class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max = 0
        if len(prices) == 1:
            return 0
        while True:
            if prices[buy] > prices[sell]:
                buy = sell
                sell = sell+1
            else:
                if prices[sell] - prices[buy] > max:
                    max = prices[sell] - prices[buy]
                sell = sell+1
            if sell == len(prices) :
                break
        return max