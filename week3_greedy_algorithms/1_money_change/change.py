# Uses python3
import sys

# Let m be the input to change into coins
def get_change(m):
    currentValue = m
    numCoins = 0

    while currentValue > 0:
        if currentValue >= 10:
            currentValue = currentValue - 10
        elif currentValue < 10 and currentValue >= 5:
            currentValue = currentValue - 5
        elif currentValue < 5 and currentValue >= 1:
            currentValue = currentValue - 1
        numCoins = numCoins + 1

    return numCoins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
