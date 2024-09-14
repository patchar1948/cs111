#!/usr/bin/env python3
# patcharin Mekchang (Noon)
# 670510717
# HW02_1
# 204111 Sec 003
# TA P'Ta

import math
m1 = float(input("m1:"))
b1 = float(input("b1:"))
m2 = float(input("m2:"))
b2 = float(input("b2:"))

x = (b2 - b1) / (m1 - m2)
y = (m1 * x) + b1
print("Lines intersect at ({:.2f},{:.2f})".format(x,y))

 