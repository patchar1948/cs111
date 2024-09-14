#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW11_2
# 204111 Sec 003

def main():
    split_and_merge(5)

def perm(seq1, seq2, res=()):
    if not seq1 or not seq2:
        return [">".join(seq1 + seq2 + res)]

    p1 = perm(seq1[1:], seq2, res + [seq1[0]])
    p2 = perm(seq1, seq2[1:], res + [seq2[0]])
    return p1 + p2


def split_and_merge(n: int) -> list[int]:
    bus = list(map(str, range(1, n + 1)))
    bus = list(zip(bus, bus[::-1]))

    bus = bus[:len(bus) // 2]

    res = set()
    for ps in bus:
    
    print(bus)


if __name__ == '__main__':
    main()