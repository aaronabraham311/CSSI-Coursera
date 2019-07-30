# Uses python3
'''
LOGIC
- Split up the expression into subexpressions and find their maximum and minimum values
- Conduct the operation on the maximum and minimum values and maximize it. 
- Continue until you have reached the final expression and output the maximum value
'''

from math import inf
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

# Finds minimum and maximum solutions from array
def min_max(i, j, m, M, op):
    temp_min = inf
    temp_max = -inf

    for k in range(i, j):
        a = evalt(M[i][k], m[k + 1][j], op[k])
        b = evalt(m[i][k], m[k + 1][j], op[k])
        c = evalt(M[i][k], M[k + 1][j], op[k])
        d = evalt(m[i][k], M[k + 1][j], op[k])

        temp_min = min(a, b, c, d, temp_min)
        temp_max = max(a, b, c, d, temp_max)

    return(temp_min, temp_max)

def get_maximum_value(dataset):

    # Splitting input into operations and numbers
    op = dataset[1: len(dataset): 2]
    d = dataset[1: len(dataset) + 1: 2]
    n = len(d)

    # Initializing arrays that store minimum and maximum arrays
    m = np.zeros(shape = (n, n), dtype = int)
    M = np.zeros(shape = (n,n), dtype = int)

    # Initializing subexpressions of length 1 (diagonal):
    for i in range (0, n):
        m[i, i] = int(d[i])
        M[i, i] = int(d[i])

    # Filling in arrays
    for s in range (1, n):
        for i in range (n - s):
            j = i + s
            m[i, j], M[i, j] = min_max(i, j, m, M, op)

    return M[0, n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
