#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# Lab 09_2
# 204111 Sec 003


def main():
    test()


def life_path(n: int) -> int:
    list_int = list(map(lambda x: int(x), str(n)))
    if len(list_int) <= 1:
        return n

    head = sum(list_int)  # บวกเลขทุกตัวให้เหลือตัวเดียว

    return life_path(head)


def test():
    assert life_path(13092004) == 1
    assert life_path(7) == 7
    assert life_path(35) == 8
    print("Let's go to sleep")


if __name__ == "__main__":
    main()
