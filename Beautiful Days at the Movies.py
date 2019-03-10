#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    itr = i
    while itr <= j:
        num = reverse(str(itr))
        num = int(num)
        print(abs(itr - num) / k)
        if abs(itr - num) % k == 0:
            count += 1
        itr += 1
    return count


def reverse(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1


ijk = input().split()

i = int(ijk[0])

j = int(ijk[1])

k = int(ijk[2])

result = beautifulDays(i, j, k)
print(result)
