#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab08_1
# 204111 Sec 003

def main():
    test()


def gcd(x: int, y: int) -> int:
    # Base Case
    if y == 0: 
        return x

    # D & C
    x = abs(x)
    y = abs(y)
    min_ = min(x, y)
    max_ = max(x, y)

    num = max_ % min_

    # Combine
    return gcd(min_, num)
    

def test():
    print(gcd(19, 71))
    assert gcd(19, 71) == 1 
    assert gcd(-39, 78) == 39
    print("<3")


if __name__ == '__main__':
    main()