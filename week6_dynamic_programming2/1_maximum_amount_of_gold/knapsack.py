# Uses python3
import sys

def optimal_weight(W, w, n):
    # Creating a dynamic programming array to store all optimal solutions for all weights <= W
    dp = [None] * (n + 1)

    # Initializing values for first row and column
    for i in range(0, n + 1):
        dp[0, i] = 0
        dp[i, 0] = 0

    '''
    LOGIC:
    - If we already have an already optimal solution, then removing an item will lead to an optimal solution for a lower weight knapsack
    - However, we are not restricted of removing the item
    - Therefore, we have the following subproblem: find whether removing the item or not removing an item will lead to an increase in value
    - We will go through all possible integer weights less than the actual weight and note down the optimal combo
    '''

    # Creating loop to run through all possible sub-weights
    for i in range (1, n + 1):
        for sub_weight in range (1, W + 1):
            

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
