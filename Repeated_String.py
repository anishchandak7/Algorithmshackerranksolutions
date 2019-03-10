#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    s_len = len(s)
    if n % s_len == 0:
        new_s = s * int(n / s_len)
    elif (len(s) == 1):
        new_s = s * n
    else:
        new_s = s * int(n / s_len) + s[0:n % s_len]

    count = 0
    for item in new_s:
        if (item == 'a'):
            count += 1

    return count


s = input()

n = int(input())

result = repeatedString(s, n)

print(result)