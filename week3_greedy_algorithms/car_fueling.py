# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefill = 0
    currentRefill = 0

    while currentRefill < len(stops):
        lastRefill = currentRefill

        while(currentRefill < len(stops) and (stops[currentRefill + 1] - stops[lastRefill] <= tank)):
            currentRefill += 1

        if currentRefill == lastRefill:
            return -1

        if currentRefill <= len(stops):
            numRefill += 1

    return numRefill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
