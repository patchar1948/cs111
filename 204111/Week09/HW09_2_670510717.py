#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# HW09_2
# 204111 Sec 003


def main():
    test()


def median_of_median(list_a: list[float]) -> float:

    len_list_a = len(list_a)
    n = len_list_a // 3
    list_b = list_a[:n]
    list_c = list_a[n : (n * 2)]
    list_d = list_a[2 * n :]
    # print(list_b, list_c, list_d)

    if len(list_b) <= 1:
        median_1 = list_b
    elif len(list_b) == 2:
        median_1 = [sum(list_b) / 2]
    elif len(list_b) == 3:
        x = max(list_b)
        y = min(list_b)
        median = sum(list_b) - (x + y)
        median_1 = [median]
    else:
        median_1 = [median_of_median(list_b)]

    if len(list_c) <= 1:
        median_2 = list_c
    elif len(list_c) == 2:
        median_2 = [sum(list_c) / 2]
    elif len(list_c) == 3:
        x = max(list_c)
        y = min(list_c)
        median = sum(list_c) - (x + y)
        median_2 = [median]
    else:
        median_2 = [median_of_median(list_c)]

    if len(list_d) <= 1:
        median_3 = list_d
    elif len(list_d) == 2:
        median_3 = [sum(list_d) / 2]
    elif len(list_d) == 3:
        x = max(list_d)
        y = min(list_d)
        median = sum(list_d) - (x + y)
        median_3 = [median]
    else:
        median_3 = [median_of_median(list_d)]

    j = median_1 + median_2 + median_3

    if len(list_a) == 1:
        return list_a[0]
    if len(list_a) == 2:
        return sum(list_a) / 2

    # print(j)
    sum_median = sum(j) - (max(j) + min(j))
    # print(sum_median)
    return sum_median


def med_of_med(list_a: list[int]) -> float:
    if len(list_a) == 3:
        return sorted(list_a)[1]
    elif len(list_a) == 2:
        return sum(list_a) / 2
    elif len(list_a) == 1:
        return list_a[0]
    else:
        pos = len(list_a) // 3

        return med_of_med(
            [
                med_of_med(list_a[:pos]),
                med_of_med(list_a[pos : 2 * pos]),
                med_of_med(list_a[2 * pos :]),
            ]
        )


def test():
    # assert median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]) == 21.0
    # assert median_of_median([28, 14, 12, 13, 21, 19 ,19, 32, 27, 23, 30, 16, 3]) == 21.0
    assert median_of_median([28, 14]) == 21.0
    print("Let's go to sleep")


def test_short():
    assert med_of_med([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]) == 21.0
    assert med_of_med([28, 14, 12, 13, 21, 19, 19, 32, 27, 23, 30, 16, 3]) == 21.0
    assert med_of_med([28, 14]) == 21.0


if __name__ == "__main__":
    # main()
    test_short()


# if len(list) <= 1:                         จำนวนในลิสต์ = 1
#     median_1 =  list                       เก็บค่า median
# elif len(list) == 2:                       จำนวนในลิสต์ =
#     median_1 = [sum(list) / 2]             เก็บค่า median
# elif len(list) == 3:                       จำนวนในลิสต์ = 3
#     x = max(list)
#     y = min(list)
#     median = sum(list) - (x + y)
#     median_1 = [median]                    เก็บค่า median
# else:
#     median_1 = [median_of_median(list)]    นำกลับไปแบ่งใหม่ให้จำนวน len(list) เป็น 1, 2 หรือ 3
