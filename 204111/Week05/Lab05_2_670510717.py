#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab05_2
# 204111 Sec 003

def main():
    
    test_count_down_to_songkran()
    
def leap_year(y):
    if (y % 4 == 0):
        if (y % 400 == 0):
            return 1 #ถ้าเป็น leap year ให้เก็บค่า 1
        elif (y % 100 == 0):
            return 0 #ถ้าไม่เป็น leap year ให้เก็บค่า 0
        else:
            return 1
    else:
        return 0

def count_down_to_songkran(d: int, m: int, y: int) -> int:
    lp = leap_year(y)
    lp1 = leap_year(y + 1)

    # หาวันที่เทียบเป็นวันในปี
    def day_of_year(d, m):
        days = 0
        if m == 1:
            days = d
        if m == 2:
            days = 31 + d
        if m == 3:
            days = 59 + d + lp
        if m == 4:
            days = 90 + d + lp
        if m == 5:
            days = 120 + d + lp
        if m == 6:
            days = 151 + d + lp 
        if m == 7:
            days = 181 + d + lp
        if m == 8:
            days = 212 + d + lp
        if m == 9:
            days = 243 + d + lp
        if m == 10:
            days = 273 + d + lp 
        if m == 11:
            days = 304 + d + lp 
        if m == 12:
            days = 334 + d + lp 
        return days
        


    days = day_of_year(d,m)

    # ระยะห่างของวัน หาได้จาก 103(ระยะห่างตั้งแต่วันที่ 1 มกรา  ถึง 13 เมษา) + ปีนั้นเป็น leap year มั้ย - จำนวนวันที่ผ่านมา
    diff_day = abs((103 + lp - days))
    # ระยะห่างของวัน (หาได้จาก 365 วัน - ปีนั้นเป็น leap year มั้ย - จำนวนวันที่ผ่านมา) + 103(ตั้งแต่วันที่ 1 มกรา  ถึง 13 เมษา) + ปีหน้าเป็น leap year มั้ย
    diff_day1 = abs((365 + lp - days) + 103 + lp1)

    # print(days,diff_day,diff_day1)
    #print(diff_day,diff_day1)
        

    if days == 103 + lp:
        return 0

    elif days < 103 + lp:
        return diff_day

    else: # day > 104
        return diff_day1

def test_count_down_to_songkran():
    # print(count_down_to_songkran(14,4,799))
    # return 0
    assert count_down_to_songkran(13,4,2025) == 0
    assert count_down_to_songkran(13,4,2024) == 0
    assert count_down_to_songkran(13,4,2023) == 0
    assert count_down_to_songkran(1,2,2024) == 72 
    assert count_down_to_songkran(4,2,2025) == 68 
    assert count_down_to_songkran(1,1,2024) == 103
    assert count_down_to_songkran(12,4,2024) == 1
    assert count_down_to_songkran(12,4,2025) == 1
    assert count_down_to_songkran(15,2,2024) == 58
    assert count_down_to_songkran(31,3,2024) == 13
    assert count_down_to_songkran(20,3,2024) == 24
    assert count_down_to_songkran(14,4,2024) == 364
    assert count_down_to_songkran(14,4,2025) == 364
    assert count_down_to_songkran(14,4,2023) == 365
    assert count_down_to_songkran(29,2,2024) == 44
    assert count_down_to_songkran(31,12,2024) == 103
    assert count_down_to_songkran(31,12,2025) == 103
    assert count_down_to_songkran(31,12,2023) == 104
    assert count_down_to_songkran(27,10,2023) == 169
    assert count_down_to_songkran(27,10,2024) == 168
    assert count_down_to_songkran(31,10,2024) == 164
    assert count_down_to_songkran(13,10,2024) == 182
    assert count_down_to_songkran(13,10,2023) == 183
    assert count_down_to_songkran(13,10,2023) == 183
    assert count_down_to_songkran(23,8,2023) == 234
    assert count_down_to_songkran(1,4,1600) == 12
    assert count_down_to_songkran(1,4,1600) == 12
    assert count_down_to_songkran(22,7,3000) == 265
    assert count_down_to_songkran(11,11,11) == 154
    assert count_down_to_songkran(14,4,99) == 364 # หาร 4 ลงตัวแต่หาร 400 ไม่ลงตัว
    
    print("all ok!")
    

if __name__ == "__main__":
    main()