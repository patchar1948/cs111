#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW02_3
# 204111 Sec 003
# TA P'Kla

import math
op = float(input("Old price: "))
a = op - 50
b = a // 100
c = (b * 100) + 98

print("New price:", int(c))