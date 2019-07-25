import numpy as np

# Uses python3
def edit_distance(s, t):

    # Creating array to store edit distances:
    rows = len(s)
    columns = len(t)

    d = np.zeros(shape=(rows + 1, columns + 1), dtype=int)

    for i in range(rows + 1):
        d[i, 0] = i

    for i in range(columns + 1):
        d[0, i] = i

    '''
    Dynamic programming logic:
    - To match one string to another, you can either insert, delete, mismatch or match 
    - The DP array (d) stores the number of insertions/deletions/mismatches/matches it takes to get 
    to a subsequence of a string (starting from the beginning)
    - By getting to the end of the DP array, we will need to use previous solutions for the number of edits
    '''
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):

            # Finding the optimal edit depending on whether last character of both strings match
            if s[i - 1] == t[j - 1]:
                d[i, j] = d[i - 1, j - 1]
            else:
                d[i][j] = 1 + min(d[i - 1, j], d[i - 1, j - 1], d[i, j - 1]) # Selecting mismatch, insertion or deletion

    # Returning very last entry of DP array
    return d[rows, columns]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
