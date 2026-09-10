class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        r,l =1,0
        n = len(prices)
        while r < n:
            cur = prices[r] - prices[l]
            print(f"{prices[l]} and {prices[r]}")
            if cur < 0:
                l = r
                r+=1
            else:
                res = max(res,cur)
                r+=1
        return res   
    