# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)

    # If element not found
    if right <= left:
        return -1
    else:
        # Creating middle point
        mid = round(left + (right-left)/2)

        # Splitting up array and calling function recursively
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return binary_search(a[0:mid], x)
        else:
            return binary_search(a[mid + 1: right], x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
