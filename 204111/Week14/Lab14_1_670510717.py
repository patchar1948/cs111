#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab14_1
# 204111 Sec 003

def main():
    # list_x = ['11/กันยายน/2643']
    # sort_date(list_x, True)
    # print('---')
    # print(list_x)

    list_x = ['11/ม.ค./2543', '11/ม.ค./2542', '11/ม.ค./2546']
    sort_date(list_x, True)
    print('---')
    print(list_x)

def parse_date(list_x: list[str]):
    # สร้าง dict ที่เก็บเดือน
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
    "ธ.ค.": 12,
    }

    # day, month, year = date_str.split('/') # 
    l_x = list(map(lambda x: x.split('/'), list_x[:]))
    result = []
    for i in l_x:
        result += [(int(i[2]), months_dict[i[1]], int(i[0]))]
    return result


def sort_date(list_x: list[str], show_steps: bool=False):

    months_dict = {
    1: "ม.ค.",
    2: "ก.พ.",
    3: "มี.ค.",
    4: "เม.ย.",
    5: "พ.ค.",
    6: "มิ.ย.",
    7: "ก.ค.",
    8: "ส.ค.",
    9: "ก.ย.",
    10: "ต.ค.",
    11: "พ.ย.",
    12: "ธ.ค."
    }


    # ผลลัพธ์จะต้องเรียงลาดับวันที่จากน้อยไปมาก
    l_x = parse_date(list_x)
    # sorted ปี จาก น้อย - มาก
    a = []
    for i in range(len(l_x)):
        sort = sorted(l_x[:i+1]) + l_x[i+1:] # sort yyyy -> mm -> dd ตามลำดับ

    # print(sort)
        if show_steps is True and i != 0:
            a = [f'{day}/{months_dict[month]}/{year}' for year, month, day in sort]
            result = ( f"{i}: {a}")
            print(result)
        a = [f'{day}/{months_dict[month]}/{year}' for year, month, day in sort]
        list_x[:] = a

if __name__ == '__main__':
    main()
