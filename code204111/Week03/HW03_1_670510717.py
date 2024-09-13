#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab03_2
# 204111 Sec 003

import math
def main():
    x = float(input("Input_number:"))
    print("Nearest_odd:", nearest_odd(x))


def nearest_odd(x: float) -> int:
    a = x / 2 # นำค่าตัวเลขที่นำเข้ามาหาร 2 เพื่อให้ได้ตัวเลขที่น้อยที่สุดที่ใกล้จำนวนนั้นมากที่สุด
    b = math.ceil(a) # ปัดเศษขึ้นค่าตัวเลขตัวใหม่ให้เป็นจำนวนเต็ม
    c = (b*2)-1 # นำจำนวนที่เป็นจำนวนเต็มคูณด้วย 2 เพื่อให้เป็นจำนวนคู่ หลังจากนั้นลบด้วย 1 เพื่อให้กลายเป็นจำนวนคี่ที่น้อยที่สุดที่ใกล้จำนวนนั้น

    return(c)

def test_nearest_odd() -> None:
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")



if __name__ == '__main__':
    main()






