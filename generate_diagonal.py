# Return an array containing the numbers in the n-th diagonal of Pascal's triangle, to the specified length.
def generate_diagonal(n, l):
    # Define an l*n+1 array which contains ones in the first row and last column.
    X = [[1 if i==0 or j==l-1 else 0 for j in range(0,l)] for i in range(0,n+1)]

    # Update the values of X adding the two values above.
    for i in range(1, n+1):
        for j in reversed(range(0, l-1)):
            X[i][j] = X[i-1][j] + X[i][j+1]

    # Return the last row (reverted).
    return X[-1][::-1]