"""
LeetCode 121 - Best Time to Buy and Sell Stock

Difficulty:
Easy

Concept:
Greedy

--------------------------------------------------------
Function Parameters

def maxProfit(self, prices):

self   -> Refers to the current object of the Solution class.
          LeetCode creates this object automatically.
          You don't need to pass anything for self.

prices -> A list of stock prices given by LeetCode.
          Each element represents the stock price on that day.

Example:
prices = [7,1,5,3,6,4]

Index (Day):   0 1 2 3 4 5
Price:         7 1 5 3 6 4

LeetCode automatically calls:

Solution().maxProfit([7,1,5,3,6,4])

You only need to write the logic.

--------------------------------------------------------

Problem:
Return the maximum profit that can be achieved by buying
one stock and selling it later.

Approach:
1. Store the minimum price seen so far.
2. Calculate today's profit.
3. Update the maximum profit.

Time Complexity:
O(n)

Space Complexity:
O(1)

"""

class Solution(object):
    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            # Update minimum buying price
            if price < min_price:
                min_price = price

            # Profit if sold today
            profit = price - min_price

            # Update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit
