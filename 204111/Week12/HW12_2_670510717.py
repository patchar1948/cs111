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
    for line in sys.stdin:
        print(line)

    return treasures


def total_value(treasure_type, treasures):
    total = 0

    return total


if __name__ == '__main__':
    main()
