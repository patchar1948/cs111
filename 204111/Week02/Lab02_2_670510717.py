#!/usr/bin/env python3
# patcharin Mekchang (Noon)
# 670510717
# Lab02_3
# 204111 Sec 003
# TA P'Guy, P'Ice

import math
millisecond = int(input("Input milliseconds:"))
day = millisecond // 86400000
h = millisecond - (day * 86400000)
hour = h // 3600000
m = h - (hour * 3600000)
minute = m // 60000
s = m - (minute * 60000)
second = s // 1000
millisecond = s - (second * 1000)
print(day, "day(s)," , hour, "hour(s),", minute, "minute(s)," , second, "second(s) and", millisecond, " millisecond" )