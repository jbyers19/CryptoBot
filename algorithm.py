# Imports
import time
from get_response import get_price


# Generate the initial price queue
def price_queue_init(array_length):
    array = []
    for i in range(array_length):
        array.append(get_price())
        time.sleep(1)
    print("\nInitial Price Queue:", str(array), "\n")
    return array


# Updates the price queue with the latest price
def price_queue(array):
    current_price = get_price()

    if array[-1] != current_price:
        i = 0
        array_length = len(array) - 1
        while i < array_length:
            array[i] = array[i + 1]
            i += 1
        array[array_length] = current_price
        # print("Updated Queue: ", str(array))

    return array


# Determines the price trend and whether to buy, sell, or hold
def get_trend(array):

    if array[0] >= array[1] >= array[2] < array[3] < array[4] < array[5]:
        return "Buy"

    elif array[0] <= array[1] <= array[2] > array[3] > array[4] > array[5]:
        return "Sell"

    else:
        return "Hold"
