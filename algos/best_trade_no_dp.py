def maxProfit(prices: list[int]) -> int:
    # num_days = len(prices)
    final_max_profit = 0
    # last_idx = num_days - 1

    def find_diff(buy_idx, sell_idx):
        b_price = prices[buy_idx]
        s_price = prices[sell_idx]
        return s_price - b_price if s_price > b_price else 0

    for i in range(len(prices) - 2, -1, -1):
        profit_diff = find_diff(i, i + 1)
        if profit_diff:
            final_max_profit += profit_diff
    return final_max_profit


# prices = [7,1,5,3,6,4]
prices = [1, 2, 3, 4, 5]
# prices = [7,6,4,3,1]
print(f'max: {maxProfit(prices)}')
