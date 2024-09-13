#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab03_2
# 204111 Sec 003

import math
def main():
   number = int(input("Number:"))
   k = int(input("Position:"))
   vavule = int(input("Vavule:"))

   print("Output:", set_kth_digit(number, k, vavule))


def kth_digit(number: int, k: int) -> int:
    number = abs(number) # ใส่ absolute ที่จำนวนที่ input เข้ามา เพื่อให้เป็นจำนวนเต็มบวก
    a = number % (10)**(k+1) # นำตัวเลขที่ input เข้ามา mod ด้วย 10 ยกกำลัง ตำแหน่งที่ต้องการ +1 เพื่อเอาเลขที่อยู่ก่อนหน้าออก
    output = a // (10)**k # นำตัวเลขใหม่ที่ได้มาหารปัดเศษลงด้วย 10 ยกกำลัง ตำแหน่งที่ต้องการ เพื่อให้ได้จำนวนเต็มในที่ต้องการ
 
    return(output)


def set_kth_digit(number: int, k: int, value: int) -> int:
    output = kth_digit(number, k)
    b = output * (10)**k # นำค่า output จากฟังก์ชันแรก คูณด้วย 10 ยกกำลัง ตำแหน่งที่ต้องการ
    c = number - b # นำค่าที่คูณได้ในสมการก่อนหน้าไปลบกับตัวเลขที่ input เข้ามา
    d = c + (value * (10)**k ) # เลขค่าใหม่หาได้จากตัวเลขที่ลบกับหลักที่ต้องการเปลี่ยนแล้ว บวกด้วยค่าที่ต้องการเปลี่ยนคูณด้วย 10 ยกกำลัง ตำแหน่งที่ต้องการ

    return(d)


if __name__ == '__main__':
    main()
