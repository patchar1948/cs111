#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab14_1
# 204111 Sec 003
def main():
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    sort_date(list_x, True)
    print('---')
    print(list_x)

# def insertion_sort(list_a):
#     size = len(list_a)
#     a = list_a[:]
#     for i in range(1, size):
#         j = i
#         while j > 0 and less_than(a[j], a[j - 1]):
#             a[j], a[j - 1] = a[j- 1], a[j]
#             j -= 1
#     return a

def less_than(date1, date2):
    months_dict = {
    "ม.ค.": 1,
    "ก.พ.": 2,
    "มี.ค.": 3,
    "เม.ย.": 4,
    "พ.ค.": 5,
    "มิ.ย.": 6,
    "ก.ค.": 7,
    "ส.ค.": 8,
    "ก.ย.": 9,
    "ต.ค.": 10,
    "พ.ย.": 11,
    "ธ.ค.": 12
    }

    day1, month1, year1 = date1.split('/')
    day2, month2, year2 = date2.split('/')
    d1 = int(day1)
    d2 = int(day2)
    m1 = months_dict[month1]
    m2 = months_dict[month2]
    y1 = int(year1)
    y2 = int(year2)
    if y1 > y2:
        return False
    elif y1 == y2:
        if m1 > m2:
            return False
        elif m1 == m2:
            if d1 > d2:
                return False
    return True


def sort_date(list_x: list[str], show_steps: bool=False):
    size = len(list_x)
    a = list_x[:]
    for i in range(1, size):
        j = i
        while j > 0 and less_than(a[j], a[j - 1]):
            a[j], a[j - 1] = a[j- 1], a[j]
        
            j -= 1
        if show_steps is True:
            # a = [f'{day}/{months_dict[month]}/{year}' for year, month, day in sort]
            result = ( f"{i}: {a}")
            print(result)

        list_x[:] = a
    # return a


if __name__ == '__main__':
    main()
