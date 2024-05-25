def MaxProfit(prices):
    buy = prices[0]
    profit = 0

    for price in range(len(prices)):
        if prices[price] < buy:
            buy = prices[price]
        elif prices[price] - buy > profit:
            profit = prices[price] - buy
    return profit

print(MaxProfit([7, 1, 5, 3, 6, 4])) # Output = 5
print(MaxProfit([7, 6, 4, 3, 1])) # Output = 0
