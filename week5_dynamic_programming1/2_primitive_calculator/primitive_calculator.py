# Uses python3
import sys

'''
LOGIC
- Go from 1 all the way to n and check the optimal solutions for each number in sequence
- Store the optimal solution in a DP array
- Backtrack to figure out how many steps it takes to reach 1
'''
def dp_optimal_sequence(n):
    # Creating array to store optimal solutions
    dp_array = [None] * (n + 1)
    optimal_sequence = [None] * (n + 1)

    # Base cases
    dp_array[0] = 0
    dp_array[1] = 0
    optimal_sequence[0] = 0
    optimal_sequence[1] = 0

    # Looping through all numbers from 1 to n
    for i in range(2, n + 1):
        # Making initial optimal solution extremely large
        dp_array[i] = 1000

        # Going through each method and noting down which method is faster
        for j in range(0, 3):
            if j == 0: # Checking +1 move
               prev_optimal_solution = dp_array[i - 1] + 1
            elif j == 1: # Checking *2 move
                if i % 2 == 0:
                    print(i)
                    prev_optimal_solution = dp_array[i // 2] + 1
            else: # Checking *3 move
                if i % 3 == 0:
                    prev_optimal_solution = dp_array[i // 3] + 1

            if prev_optimal_solution < dp_array[i]:
                dp_array[i] = prev_optimal_solution
                optimal_sequence[i] = j # Storing optimal move

    return dp_array, optimal_sequence.reverse()


def greedy_optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
dp_array, optimal_sequence = dp_optimal_sequence(n)

# Minimum number of operations
print(dp_array[len(dp_array) - 1])

# List of numbers leading to final number n
num_list = []
num = n

for i in optimal_sequence:
    num_list.append(num)

    if i  == 0:
        num -= 1
    elif i == 1:
        num /= 2
    else:
        num /= 3

# Printing out numbers
num_list.reverse()

for x in num_list:
    print(x, end=' ')