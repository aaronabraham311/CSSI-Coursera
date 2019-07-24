# Uses python3
def edit_distance(s, t):
    # Creating array to store edit distances:
    rows = len(s)
    columns = len(t)

    d = []

    # Populating DP array
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(0)
        d.append(row)

    for i in range(rows):
        d[i][0] = i

    for i in range(columns):
        d[0][i] = i

    '''
    Dynamic programming logic:
    - To match one string to another, you can either insert, delete, mismatch or match 
    - The DP array (d) stores the number of insertions/deletions/mismatches/matches it takes to get 
    to a subsequence of a string (starting from the beginning)
    - By getting to the end of the DP array, we will need to use previous solutions for the number of edits
    '''
    for j in range(columns):
        for i in range(rows):

            # Calculating the number of edits to get to subsequence for each type of edit
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            mismatch = d[i - 1][j - 1] + 1
            match = d[i - 1][j - 1]

            # Finding the optimal edit depending on whether last character of both strings match
            if s[i] == t[j]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)

    # Returning very last entry of DP array
    return d[rows - 1][columns - 1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
