#!/usr/bin/env python3
# patcharin Mekchang (Noon)
# 670510717
# Lab02_1
# 204111 Sec 003
# TA P'Kla, P'Guy

import math

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
s = (a + b + c ) / 2
area = math.ceil((s * (s - a) * (s - b) * (s - c)) ** 0.5) 
print("area:", area)

