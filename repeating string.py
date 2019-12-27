import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    no=0
    for i in s:
        if i == 'a':
            no+=1
    res=no*(n / len(s))
    for i in s[:n % len(s)]:
        if i == 'a':
            res+=1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input().strip()

    n = long(raw_input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
