import math

# Return an array containing the numbers in the n-th diagonal of Pascal's triangle, to the specified length.
def generate_diagonal(n, l):
    diagonal = []
    for k in range(0, l):
        diagonal.append( math.comb(n+k, k) )

    return diagonal
