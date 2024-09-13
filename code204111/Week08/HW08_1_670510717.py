#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW08_1
# 204111 Sec 003

from math import isclose

def main():
    test_pi()

def pi(n: int) -> float:
    # Base Case
    if n == 0:
        return 3

    # Divide & Conquer
    head = 4 / ((n * 2) * ((n * 2) + 1) * ((n * 2) + 2))
    tail = pi(n - 1)

    # Combine
    if n % 2 == 0:
        return tail - head

    else:
        return tail + head


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("Let's go to bed")


if __name__ == '__main__':
    main()