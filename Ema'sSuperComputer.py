# Prepare -> Algorithms -> Implementation -> Ema's Super Computer

#!/bin/python3

import os

# The function returns the product of the two non-overlapping plusses with the highest surface area, as an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.

def twoPluses(grid):
    l = len(grid)
    w = len(grid[0])
    plus = []
    if(min(l, w) == 2) :
        g = sum([i.count('G') for i in grid])
        if(g > 0) :
            return 1
        else :
            return 0
    else :
        for i in range(l) :
            for j in range(w) :
                if(grid[i][j] == 'G') :
                    area = 1
                    plus.append([area, i, j])
                    for k in range(1, (min(l, w) + 1) // 2) :
                        if(i - k >= 0 and j - k >= 0 and i + k <= l - 1 and j + k <= w - 1) :
                            if(grid[i - k][j] == grid[i + k][j] == grid[i][j - k] == grid[i][j + k] == 'G') :
                                area += 4
                                plus.append([area, i, j])
                            else :
                                break
    plus.sort(key = lambda row : (row[0], -row[1], -row[2]), reverse = True)
    product = []
    for i in range(len(plus)) :
        for j in range(i + 1, len(plus)) :
            if(plus[i][1] != plus[j][1] or plus[i][2] != plus[j][2]) :
                size1 = (plus[i][0] // 4) + 1
                size2 = (plus[j][0] // 4) + 1
                min_dist = size1 + size2 - 1
                if(plus[i][1] == plus[j][1] or plus[i][2] == plus[j][2]) :
                    if(abs(plus[i][1] - plus[j][1]) >= min_dist or abs(plus[i][2] - plus[j][2]) >= min_dist) :
                        product.append(plus[i][0] * plus[j][0])
                else :
                    if(abs(plus[i][1] - plus[j][1]) >= size1 or abs(plus[i][2] - plus[j][2]) >= size1) :
                        product.append(plus[i][0] * plus[j][0])
                    elif(abs(plus[i][1] - plus[j][1]) >= size2 and abs(plus[i][2] - plus[j][2]) >= size2) :
                        product.append(plus[i][0] * plus[j][0])
    return (max(product) if len(product) > 0 else 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
