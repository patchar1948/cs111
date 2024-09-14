#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

from functools import reduce

def find_min(list_a: list[int]) -> int:
    return reduce(lambda x, y:x if x < y else y, list_a)


if __name__ == '__main__':
    assert find_min([0, 1, 2, 3]) == 0
    assert find_min([11, 10, 12, 13]) == 10
    print('ALL OK')
