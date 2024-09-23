from typing import List


class Soluton:
    def maxProfit(self, prices: List[int]) -> int:
        # we will iterate through list. Keep a record of lowest. 
        max_profit = 0

        lowest = prices[0]
        for current_price in prices:
            if current_price < lowest:
                lowest = current_price
            max_profit = max(max_profit, current_price - lowest)
        return max_profit
