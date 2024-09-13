#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003


def reverse_cap(list_a):
    return list(map(lambda x:x[0].lower() + x[1:].upper(), list_a))


if __name__ == '__main__':
    assert reverse_cap(['I', 'bought', 'two', 'bananas']) == \
        ['i', 'bOUGHT', 'tWO', 'bANANAS']

    print("All OK!")
