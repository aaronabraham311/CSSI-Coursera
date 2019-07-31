# Uses python3
import sys

def get_majority_element(a, left, right):

    # Base cases (either array has size 1 or 2)
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    # Recursive calls to get majority element in left and right subarrays
    left_majority_element = get_majority_element(a, left, ((left + right - 1) // 2) + 1)
    right_majority_element = get_majority_element(a, ((left + right - 1) // 2) + 1, right)

    # Finds out how many values in whole list correspond to right/left majority element
    left_count = 0
    right_count = 0
    for i in range(left, right):
        if a[i] == left_majority_element:
            left_count += 1
        elif a[i] == right_majority_element:
            right_count += 1

    # If there is more counts of the left_majority/right_majority element than half of the array length, then it must be in majority
    if left_count > (right - left) // 2:
        return left_majority_element
    elif right_count > (right - left) // 2:
        return right_majority_element

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
