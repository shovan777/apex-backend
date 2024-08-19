def maxProfit(prices: list[int]) -> int:
    num_days = len(prices)
    profits = [0] * num_days
    final_max_profit = 0
    last_idx = num_days - 1
    def find_diff(buy_idx, sell_idx):
        b_price = prices[buy_idx]
        s_price = prices[sell_idx]
        return s_price - b_price if s_price > b_price else 0

    for i in range(last_idx, -1, -1):
        # profits[i] += max([find_diff(i, j)+profits[j] for j in range(i+1, num_days)] + [0])
        max_profit = 0
        for j in range(i+1, num_days):
            profit = find_diff(i,j) + profits[j]
            if profit > max_profit:
                max_profit = profit
        profits[i] += max_profit
        if max_profit > final_max_profit:
            final_max_profit = max_profit
    # print(profits)
    return final_max_profit

# prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
print(f'max: {maxProfit(prices)}')


