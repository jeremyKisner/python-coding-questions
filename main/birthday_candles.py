#!/bin/python3

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    all_candles = {}
    for candle in candles:
        if candle not in all_candles:
            all_candles[candle] = 1
        else:
            all_candles[candle] += 1
    print(all_candles.get(max(all_candles)))
    return all_candles.get(max(all_candles))

if __name__ == '__main__':
    candles = [3, 2, 1, 3]
    result = birthdayCakeCandles(candles)
