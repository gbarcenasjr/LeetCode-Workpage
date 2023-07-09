"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

def maxProfit(prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return int(max_profit)

if __name__ == '__main__':
    example = [7,1,5,3,6,4]
    print(maxProfit(example))

"""
Intuition
If we want to maximize the profit, we should buy the stock at the lowest possible price and sell it at the highest price after that day. We need to find these two prices in the list.

Approach
First, we initialize 'min_price' to be infinity and 'max_profit' to be 0. We iterate through the list of prices: if we find a price that is less than 'min_price', we update 'min_price'. If the difference between the current price and 'min_price' is greater than 'max_profit', we update 'max_profit'. This ensures we're always buying at the lowest price seen so far, and selling at the highest price that occurs after the lowest price was seen.

Time complexity: O(n)
We iterate through the list of prices once, where n is the length of the list, which results in a linear time complexity.

Space complexity: O(1)
We use only a constant amount of space to store 'min_price' and 'max_profit', regardless of the input size, so the space complexity is constant.
"""