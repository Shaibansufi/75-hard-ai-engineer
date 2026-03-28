# Best Time to Buy and Sell
class Solution:
    
    def maxProfit(self,prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit,price-min_price)
        return max_profit

solution = Solution()
print(solution.maxProfit([5,2,6,1,4]))

