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
    optimal_sequence = [5] * (n + 1)

    # Base cases
    dp_array[0] = 0
    dp_array[1] = 0

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
                    prev_optimal_solution = dp_array[i // 2] + 1
            else: # Checking *3 move
                if i % 3 == 0:
                    prev_optimal_solution = dp_array[i // 3] + 1

            if prev_optimal_solution < dp_array[i]:
                dp_array[i] = prev_optimal_solution
                optimal_sequence[i] = j # Storing optimal move

    # Reversing list
    optimal_sequence.reverse()

    return dp_array, optimal_sequence


input = sys.stdin.read()
n = int(input)
dp_array, optimal_sequence = dp_optimal_sequence(n)

# Minimum number of operations
print(dp_array[len(dp_array) - 1])



# List of numbers leading to final number n
num_list = []
num = n
newNum = 0

i = 0

# LOGIC: Based on the operation saved in optimal_sequence, we will divide the orginal number down to zero
# while saving intermediate numbers in num_list
while True:
    num_list.append(num)
    divisor = optimal_sequence[i]

    if num == 1:
        break
    else:
        if divisor == 0:
            newNum = num - 1
        elif divisor == 1:
            newNum = num / 2
        else:
            newNum = num / 3

    difference = num - newNum
    i = int(i + difference)
    num = newNum

# Printing out numbers
num_list = reversed(num_list)

for x in num_list:
    print(int(x), end=' ')