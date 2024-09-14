#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW06_3
# 204111 Sec 003

def main():
    test_moving_average()
    # list_x = [1, 2, 3, 4, 5]
    # win_size = 2
    # moving_average(list_x, win_size)


def moving_average(list_x: list[float], win_size: int) -> list[float]:
    if win_size > len(list_x): # ถ้าค่า win_size มากกว่าค่า list ทั้งหมด
        return []

    ranger = (len(list_x) - win_size) + 1 # หาจำนวนรอบสูงสุดที่สามารถหาได้
    l_a = list(range(0, ranger)) # สร้าง list ใช้ในการระบุตำแหน่ง
    
    # ค่ากลางแต่ละตัวหาได้จาก การหาผลรวมของตำแหน่งที่ x จนถึงตำแหน่งที่ x + win_size หารด้วย win_size
    average = list(map(lambda x:(sum(list_x[x : x + win_size])) / win_size, l_a)) 

    # print(average)
    return(average)

def test_moving_average():
    assert moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]
    print(':)')
    
    
if __name__ =='__main__':
    main()