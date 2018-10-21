# Imports
from algorithm import *
from get_response import get_price
from trade import *

import time
import datetime
import sys


# Send all print()s to stdout
sys.stdout = open("./CryptoBot.txt", "w")


# Timestamp
def timestamp():
    print("Time:",
          datetime.datetime.fromtimestamp(
              int(time.time())
          ).strftime('%Y-%m-%d %H:%M:%S')
          )


# Variables
capital = 0.00
num_coins = 1000.000000000
price = 0.00


# Main method
def main():
    global capital, num_coins, price
    trend = price_queue_init(6)

    while True:
        trend = price_queue(trend)
        trade_status = get_trend(trend)
        price = trend[-1]

        if trade_status == "Buy" and capital > 0:
            timestamp()
            price = get_price()
            num_coins = buy(capital, price)
            capital = 0.00
            print("\n-- Bought coins! --\n")
            print("Capital: %s BTC" % str(capital))
            print("Number of Coins:", num_coins)
            print("Current price: %s BTC" % str(price))
            print("\n=================================================\n")

        elif trade_status == "Sell" and num_coins > 0:
            timestamp()
            price = get_price()
            capital = sell(price, num_coins)
            num_coins = 0
            print("\n-- Sold coins! --\n")
            print("Capital: %s BTC" % str(capital))
            print("Number of Coins:", num_coins)
            print("Current price: %s BTC" % str(price))
            print("\n=================================================\n")

        else:
            pass


        time.sleep(5)


# Start script if main
if __name__ == '__main__':
    main()
