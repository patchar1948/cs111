#!/usr/bin/env python3
# patcharin
# 670510717
# Sec003

def count_4n5(n):
    a = list(filter(lambda x: '4' in str(x) and '5' in str(x), range(n+1)))
    # print(a)
    b = len(list(filter(lambda x: '4' in str(x) and '5' in str(x), range(n+1))))
    # print(b)
    return b


if __name__ == '__main__':
    assert count_4n5(99) == 2
    print("All OK!")
