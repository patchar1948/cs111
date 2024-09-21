#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab12_1
# 204111 sec 003

def main():
    # print('1, 2023')
    for i in range(1,13):
        #display_calendar(i, 2023)
        pass
    # print('2, 2020')
    display_calendar(12,1999)
    # display_calendar(2,2023)
    # print('2, 2021')
    # display_calendar(2,2021)
    # print('2, 2022')
    # display_calendar(2,2022)
    # print('2, 2023')
    # display_calendar(2,2023)
    # print('2, 2024')
    # display_calendar(2,2024)
    # print('2, 2025')
    # display_calendar(2,2025)
    # print('1, 1600')
    # display_calendar(1,1600)
    # print('3, 2019')
    # display_calendar(3,2019)

def day_in_month(month, year):
    if month in [3, 5, 7, 8, 10, 12, 1]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0):
            if (year % 400 == 0):
                return 29 #ถ้าเป็น leap year
            elif (year % 100 == 0):
                return 28 # ไม่เป็น leap year
            else:
                return 29
        else:
            return 28

def display_calendar(month: int, year: int) -> None:

    days =day_in_month(month, year)

    if month == 1:
        month = 13
        year = year - 1
    if month == 2:
        month = 14
        year = year - 1
    

    q = 1 # เริ่มวันที่ 1 ของทุกเดือน
    m = month
    k = year % 100 
    j = year // 100
    h = (q + (((13 * (m + 1)) // 5)) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    # หาวันเริ่มต้น Su Mo Tu We Th Fr Sa --> 1 2 3 4 5 6 0
    keet = ["--"]
    if h == 0:
        num_keet = (keet * 6)
        # print(len(num_keet))
    else:
        num_keet = (keet * (h - 1))
        # print(len(num_keet))

    # print(len(num_keet))
    first = list(range(1, (7 - (len(num_keet) -1))))
    first = list(map(lambda x:" " + str(x) if len(str(x)) < 2 else str(x) , range(1, (7 - (len(num_keet) -1)))))
    print("Su Mo Tu We Th Fr Sa")
    line1 = num_keet + first
    line_1 = ' '.join(line1)
    print(line_1)
    line2 = list(map(lambda x:" " + str(x) if len(str(x)) < 2 else str(x), range(7 - len(num_keet) + 1, 7 - len(num_keet)+8 )))
    line_2 = ' '.join(line2)
    print(line_2)
    line3 = list(map(lambda x:" " + str(x) if len(str(x)) < 2 else str(x), range(7 - len(num_keet)+8, 7 - len(num_keet)+15 )))
    line_3 = ' '.join(line3)
    print(line_3)
    line4 = list(map(lambda x: str(x), range(7 - len(num_keet)+15, 7 - len(num_keet)+22 )))
    line_4 = ' '.join(line4)
    print(line_4)
    # print(day_in_month(month, year))
    line5 = list(map(lambda x: str(x) , range(7 - len(num_keet)+22, days + 1)))
    if len(line5) > 7:
        line_5 = line5[:7]
        line_5 = ' '.join(line_5)
        print(line_5)
        line6 = line5[7:]
        line_6 = ' '.join(line6) + '\n'
        print(line_6)
    else:
        line_5 = ' '.join(line5) + '\n'
        print(line_5) 


if __name__ =='__main__':
    main()

