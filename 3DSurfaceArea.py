#!/bin/python3

import os

# The function returns the surface area as an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.

def surfaceArea(A, H, W):
    top = bottom = H * W
    area = top + bottom
    for i in range(H) :
        for j in range(W) :
            area += max(0, A[i][j] - (A[i + 1][j] if i < H - 1 else 0))
            area += max(0, A[i][j] - (A[i][j + 1] if j < W - 1 else 0))
            area += max(0, A[i][j] - (A[i - 1][j] if i > 0 else 0))
            area += max(0, A[i][j] - (A[i][j - 1] if j > 0 else 0))
    return area
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A, H, W)

    fptr.write(str(result) + '\n')

    fptr.close()