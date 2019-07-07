# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_optimized(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        new = previous + current
        new = new % 10

        current, previous = new, current

    return current


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_optimized(n))
