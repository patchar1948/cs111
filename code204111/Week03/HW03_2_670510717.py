#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab03_2
# 204111 Sec 003

import math
def main():
     number = int(input("Number:"))
     k = int(input("Position:"))
    #assert(kth_digit(789, 0) == 9)
    #assert(kth_digit(-789, 0) == 9)
     print("Output:", kth_digit(number, k))

def kth_digit(number: int, k: int) -> int:
    number = abs(number)
    a = number % (10)**(k+1) # นำตัวเลขที่ input เข้ามา mod ด้วย 10 ยกกำลัง ตำแหน่งที่ต้องการ +1 เพื่อเอาเลขที่อยู่ก่อนหน้าออก
    output = a // (10)**k # นำตัวเลขใหม่ที่ได้มาหารปัดเศษลงด้วย 10 ยกกำลัง ตำแหน่งที่ต้องการ เพื่อให้ได้จำนวนเต็มในที่ต้องการ
 
    return(output)

if __name__ == '__main__':
    main()


