# Uses python3
import sys

def value_per_weight (weights, values):
    vpw = []

    for i in len(weights):
        vpw[i] = values[i]/weights[i]

    vpw.sort(reverse = True)

    return vpw

def get_optimal_value(capacity, weights, values):
    value = 0.
    total_weight = capacity

    # write your code here
    vpw = value_per_weight(weights, values)

    for _ in len(values):
        if capacity == 0:
            return value
        else:
            for i in len(vpw):
                min_weight = min(weights[i], total_weight)
                value = value + min_weight * vpw[i]
                total_weight = total_weight - min_weight


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
