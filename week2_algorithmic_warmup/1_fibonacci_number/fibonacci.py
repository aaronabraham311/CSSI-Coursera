# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_fast(n):
    if n <= 1:
        return n
    else:
        array = [0] * (n + 1)

        array[0] = 0
        array[1] = 1

        for i in range(2, n + 1):
            array[i] = array[i - 1] + array[i - 2]
        return array[n]

n = int(input())
print(calc_fib_fast(n))
