from typing import List

from test_framework import generic_test

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
def buy_and_sell_stock_once(prices: List[float]) -> float:
    # Hint: Identifying the min and max is not enough since the min may appear after the max height.
    # Focus on valid differences
    # BUY LOW, SELL HIGH
    # the max profit is made by selling on a specific day is determined by the 
    # min of the stock prices over the previous days 
    # TODO: return max profit that be made by buying and then selling ONE share of that stock
    min_price_so_far, max_profit = float('inf'), 0.0 # float('inf') rep max possible float number
    # min_price_so_far is essentially our left pointer which shifts when we think there's a lower
    # to buy in which we've seen so far

    for price in prices: # O(n) - checks all elements in prices[]
        # compute CURRENT max profit
        max_profit_sell_today = price - min_price_so_far # current sell - min price we're thinking to buy

        # trying to return!
        # update max_profit if the current max profit computed is greater
        # if update then you're shifting max_profit to the left
        max_profit = max(max_profit, max_profit_sell_today) # O(1) - compares two values

        # left pointer as reference of what wanna buy so far! 
        # update min_price_so_far if its the min element seen so far in the array
        # if update, then you're shifting min_price_so_far to the left
        # min(price we're thinking to buy that's cheapest, currently seeing to buy)
        min_price_so_far = min(min_price_so_far, price) # O(1) - compares two values


    return max_profit

if __name__ == '__main__':
    # prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    # print(buy_and_sell_stock_once(prices))

    # prices2 = [11, 10, 10, 10, 10]
    # print(buy_and_sell_stock_once(prices2))
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
