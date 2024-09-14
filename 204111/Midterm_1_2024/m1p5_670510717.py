#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

import math
EPSILON = 10**-3

def median(list_a: list[int]) -> float:
    list_a = sorted(list_a)
    len_list_a = len(list_a)

    index = (len_list_a // 2)

    if len_list_a %  2 != 0:
        return list_a[index]
    else:
        return (list_a[index - 1] + list_a[index]) / 2


if __name__ == '__main__':
    # print(median)
    assert math.isclose(median([1, 2, 3]), 2, abs_tol=EPSILON)
    assert math.isclose(median([3, 2, 1, 0]), 1.5, abs_tol=EPSILON)
    print('ALL OK!')
