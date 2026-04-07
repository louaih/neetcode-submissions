class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > curr_max:
                    curr_max = profit
        

        return curr_max
