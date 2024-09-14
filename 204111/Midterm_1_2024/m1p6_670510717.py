#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

def main():
    a = [1,2,3,4]
    print(adjacent_sum(a))
    print(adjacent_sum(a))

def adjacent_sum(list_a: list[int], start = 0, list_sum = []) -> list[int]:
    if len(list_a) == list_sum:
        return []
    if len(list_sum) == len(list_a) - 1:
        return list_sum

    head = [list_a[start] + list_a[start + 1]]
    start = start + 1
    list_sum = list_sum + head

    # print(list_sum)
    return adjacent_sum(list_a, start, list_sum)


if __name__ == '__main__':
    main()
    assert adjacent_sum([0, 1, 2]) == [1, 3]
    assert adjacent_sum([2, 4, 6, 8]) == [6, 10, 14]
    print('ALL OK')
