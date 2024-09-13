#!/usr/bin/env python3
# patcharin Mekchang (Noon)
# 670510717
# HW02_2
# 204111 Sec 003
# TA P'Ta

import math
x = int(input("x: "))
y = int(input("y: "))
x = x - 1

sum_1 = (x * (x + 1) * ((2 * x ) + 1)) / 6 
sum_2 = (y * (y + 1) * ((2 * y ) + 1)) / 6

sum_3 = sum_2 - sum_1 

print("sum is ", int(sum_3))