#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# HW09_1
# 204111 Sec 003

from functools import reduce


def main():
    test()


def left_max(list_a: list[int], list_max=[], start=0) -> list[int]:
    # if start >= len(list_a):
    #     return list_max

    if len(list_max) == len(list_a) - 1:
        return [list_a[0]] + list_max  # เพิ่มตำแหน่งที่ 0 เข้าไป ->  [3] + [3, 3, 3, 3, 4]

    head = reduce(lambda x, y: max(x, y), list_a[: start + 2])
    list_max = list_max + [head]  # list_max = [3, 3, 3, 3, 4]
    start = start + 1

    return left_max(list_a, list_max, start)


def test():
    assert left_max([-1, -0, 1]) == [-1, -0, 1]
    assert left_max([3, 3, 1, 1, 2, 4]) == [3, 3, 3, 3, 3, 4]
    print("Let's go to sleep")


if __name__ == "__main__":
    main()


# head = reduce(lambda x, y:max(x,y), list_a[start:start + 2])
