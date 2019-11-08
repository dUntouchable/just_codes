'''
Davis has a number of staircases in his house and he likes to climb each staircase , , or  steps at a time. 
Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.

stairs = [0]*37
stairs[0] = 1
stairs[1] = 1

def stepPerms(n):
    if n < 0:
        return 0

    if stairs[n] != 0:
        return stairs[n]
        
    val = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    if stairs[n] == 0:
        stairs[n] = val

    return val



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
