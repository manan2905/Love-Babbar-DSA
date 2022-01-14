import sys

"""
17. BEST TIME TO BUY AND SELL STOCK
Ek variable maintain karo jo curr element se pehle ki minimum value ka track rakhega

"""


def best_buy(prices):
    # this variable is storing the minimum value of the left part of the array
    mini = sys.maxsize
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < mini:
            mini = prices[i]
        else:
            profit = prices[i] - mini
            if max_profit < profit:
                max_profit = profit
    return max_profit


arr = [int(i) for i in input().split()]
print(best_buy(arr))
