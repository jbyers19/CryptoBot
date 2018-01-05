# Imports
from decimal import *


# Buy coins
def buy(capital, price):
    print("Number of coins bought: " + str(Decimal(capital) / Decimal(price)))
    return Decimal(capital) / Decimal(price)


# Sell coins
def sell(price, amount):
    print("Number of coins sold: " + str(Decimal(price) * Decimal(amount)))
    return Decimal(price) * Decimal(amount)
