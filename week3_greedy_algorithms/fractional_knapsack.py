# Uses python3
import sys

# Creating array of unit value per weight for each object
def value_per_weight (weights, values):
    vpw = []

    # Appending corresponding weights and values into one array
    for i in range(0, len(weights)):
        vpw.append((values[i], weights[i]))

    # Sorting based on value/weight
    vpw.sort(key = lambda x: x[0]/x[1], reverse = True)

    return vpw

def get_optimal_value(capacity, weights, values):
    value = 0.
    total_weight = capacity

    # write your code here

    # Array of all values per unit weight
    vpw = value_per_weight(weights, values)

    # Loops through and puts in object in knapsack for all objects
    for obj_value, obj_weight in vpw:
        if total_weight == 0:
            return value
        else:
            min_weight = min(obj_weight, total_weight)
            value += min_weight * (obj_value/obj_weight)
            total_weight -= min_weight


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
