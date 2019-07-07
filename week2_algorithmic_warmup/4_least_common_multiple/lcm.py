# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_optimized(a, b):
    if b == 0:
        return a
    a_prime = a % b

    return gcd_optimized(b, a_prime)

def lcm_optimized(a, b):
    gcd = gcd_optimized(a, b)

    return (round((a * b)/gcd))

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm_optimized(a, b))

