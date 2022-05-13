# Prepare -> Algorithms -> Implementation -> Larry's Array

#!/bin/python3

import os

# The function returns "YES" if the array can be sorted according to the given conditions or "NO" if the array cannot be sorted.
# The function accepts INTEGER_ARRAY A as parameter.

def larrysArray(A):
    if(A == sorted(A)) :
        return "YES"
    else :
        sum = 0
        for i in range(len(A)) :
            for j in range(i + 1, len(A)) :
                if(A[i] > A[j]) :
                    sum += 1
        if(sum % 2 == 0) :
            return "YES"
        else :
            return "NO"
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
