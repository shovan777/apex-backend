def maxProfit(prices: list[int]) -> int:

    def best_profit(idx, max_val):
        # print(f'max_Val: {max_val}')
        # ahile ko max profit
        # ani min val sanga diff compare hai
        next_price = prices[idx + 1]
        if next_price > max_val:
            max_val = next_price
        return max_val

    max_val = prices[-1]
    max_profit = 0
    for i in range(len(prices)-2, -1, -1):
        max_val = best_profit(i, max_val)
        profit = max_val - prices[i]
        print(f'{profit}, {max_val}, {prices[i]}')
        if profit > max_profit:
            max_profit = profit

    return max_profit

q1 = [7,1,5,3,6,4]
print(f'max: {maxProfit(q1)}')
