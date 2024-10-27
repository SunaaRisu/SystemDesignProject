#!/usr/bin/env python3
import time
# import sys

x = 2

# sys.set_int_max_str_digits(1000000)

t1 = time.time()
while x < (10 ** 100000):
    x = x ** 2
    print(x)
t2 = time.time()

print('Needed:', t2 - t1, 'seconds')

input()
