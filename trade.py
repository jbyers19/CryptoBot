# Imports
from decimal import *


# Buy coins
def buy(capital, price):
    print("%s of coins bought for %s" % (str(Decimal(capital) / Decimal(price)), str(price)))
    return Decimal(capital) / Decimal(price)


# Sell coins
def sell(price, amount):
    print("%s of coins sold for %s\nProfit: %s BTC " % (str(amount), str(price), str(Decimal(price) * Decimal(amount))))
    return Decimal(price) * Decimal(amount)
