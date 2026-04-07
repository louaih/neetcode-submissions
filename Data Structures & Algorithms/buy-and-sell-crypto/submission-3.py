class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        left = 0
        right = 1

        for i in range(1, len(prices)):
            if(prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                if profit > curr_max:
                    curr_max = profit
            else:
                left = right
            right += 1
        
        

        return curr_max
