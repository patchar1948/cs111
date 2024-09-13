#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab10_1
# 204111 Sec 003


def main():
    test()

def longest_digit_run(n: int, a = 1, max_ = 1) -> int:
    n = str(n)
    for i in range(len(n)- 1):
        if n[i] == n[i + 1]:
            a = a + 1
        else:
            if a > max_:
                max_ = a
            # reset ค่า a
                a = 1
            else:
                max_ = max_
                a = 1
    if a > max_:
        max_ = a
    # print(max_)
    return max_

def test():
    assert longest_digit_run(11777332) == 3
    assert longest_digit_run(1177332) == 2
    assert longest_digit_run(1111111111) == 10

    print("sak tee")

if __name__ == '__main__':
    main()