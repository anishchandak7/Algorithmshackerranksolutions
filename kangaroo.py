#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
from pip._vendor.distlib.compat import raw_input


def kangaroo(x1, v1, x2, v2):
     if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
         return True
     else:
         return False

if __name__ == '__main__':
    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    if result == True:
        print("YES")
    else:
        print("NO")

