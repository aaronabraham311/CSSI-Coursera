# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefill = 0
    currentRefill = 0

    while currentRefill <= len(stops):
        lastRefill = currentRefill

        while(currentRefill <= len(stops) and (distance[currentRefill + 1] - distance[lastRefill] <= tank)):
            currentRefill += 1

        if currentRefill == lastRefill:
            return -1

        if currentRefill <= stops:
            numRefill += 1

    return numRefill


    return -1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
