#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

from math import isclose


def harmonic_mean(list_a):
    return len(list_a) / sum(list(map(lambda x:(1 / x), list_a)))


if __name__ == '__main__':
    assert isclose(harmonic_mean([1, 2, 2, 2]), 1.6, abs_tol=0.001)

    print("All OK!")