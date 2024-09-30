#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW12_2
# 204111 Sec 003

import sys


def main():
    treasures = read_input()

    assert total_value('Gold', treasures) == 1090
    assert total_value('Ruby', treasures) == -1


def read_input():
    treasures = {}
    i = 1
    # temp = list(sys.stdin)
    # print(temp)
    for line in sys.stdin:
        if line[0] == '#':
            continue
        l_s = line.split(',')
        l_s = list(map(lambda x: x.strip(',\r\n '), l_s))
        if l_s[1] in treasures:
            treasures[l_s[1]] += [(l_s[0], int(l_s[2]))]
        else:
            treasures[l_s[1]] = [(l_s[0], int(l_s[2]))]
    
        # print("round", i)
        # print(l_s)
        # i += 1
    # print(treasures)
    return treasures


def total_value(treasure_type, treasures):
    total = 0
    if treasure_type in treasures:
        for i in treasures[treasure_type]:
            total += i[1]
    else:
        total = -1
    # print(total)
    return total

if __name__ == '__main__':
    main()
