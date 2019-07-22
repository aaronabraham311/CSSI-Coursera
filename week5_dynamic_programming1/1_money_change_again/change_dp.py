# Uses python3
import sys

def get_change(m):
    # Creating array to store previous optimal solutions to money changes
    T = [100] * m
    T[0] = 0

    # Loop through money:
    for coin in range(1, m + 1):
        # Making initial solution infinitely large
        T[coin] = 100

        # Going through each coin and getting respective change
        # Remember basic change rule: change = (money - denomination) + 1 (+1 for change given)
        for denom in [1, 3, 4]:
            change = T[(coin - denom) + 1]

            # If calculated change is less than the current solution, replaces it
            if change < T[coin]:
                T[coin] = change

    return T[len(T) - 1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
