#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# HW09_2
# 204111 Sec 003

# ข้อหาค่ากลาง


def main():
    test()


def help_median_of_median(litsy):
    # if
    len_litsy = len(litsy)
    n = len_litsy // 3
    list_b = litsy[:n]
    list_c = litsy[n : (n * 2)]
    list_d = litsy[2 * n :]

    if len(list_b) == 1:
        median_1 = list_b
    if len(list_b) == 2:
        median_1 = [sum(list_b) / 2]
    if len(list_b) == 3:
        x = max(list_b)
        y = min(list_b)
        median = sum(list_b) - (x + y)
        median_1 = [median]
    else:
        median_1 = list_b

    if len(list_c) == 1:
        median_2 = list_c
    if len(list_c) == 2:
        median_2 = sum(list_c) / 2
    if len(list_c) == 3:
        x = max(list_c)
        y = min(list_c)
        median = sum(list_c) - (x + y)
        median_2 = [median]
    else:
        median_2 = list_c

    if len(list_d) == 1:
        median_3 = list_d
    if len(list_d) == 2:
        median_3 = sum(list_d) / 2
    if len(list_d) == 3:
        x = max(list_d)
        y = min(list_d)
        median = sum(list_d) - (x + y)
        median_3 = [median]
    else:
        median_3 = list_d

    print(median_1, median_2, median_3)

    # return help_median_of_median(list_b)
    # return help_median_of_median(list_c)
    # return help_median_of_median(list_d)


def test():
    assert help_median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]) == 21.0
    print("Let's go to sleep")


if __name__ == "__main__":
    main()
