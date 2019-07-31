# Uses python3
import sys
import numpy as np

def optimal_weight(W, w, n):
    # Creating a dynamic programming array to store all optimal solutions for all weights <= W
    dp = np.zeros(shape = (n, W + 1), dtype = int)

    '''
    LOGIC:
    - If we already have an already optimal solution, then removing an item will lead to an optimal solution for a lower weight knapsack
    - However, we are not restricted of removing the item
    - Therefore, we have the following subproblem: find whether removing the item or not removing an item will lead to an increase in value
    - We will go through all possible integer weights less than the actual weight and note down the optimal combo
    '''

    # Creating loop to run through all possible sub-weights
    for j in range (0, n):
        for i in range (1, W + 1):
            if w[j] > i:
                dp[j, i] = dp[j - 1, i]
            else:
                dp[j, i] = max(w[j] + dp[j - 1, i - w[j]], dp[j - 1, i])

    return dp[len(w) - 1, W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
