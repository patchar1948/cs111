#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW04_2
# 204111 Sec 003
# TA P'Ta

def main():
    h1 = int(input(""))
    m1 = int(input(""))
    p1 = str(input("AM or PM:"))
    h2 = int(input(""))
    m2 = int(input(""))
    p2 = str(input("AM or PM:"))
    
    print("Diff:", minute_diff(h1, m1, p1, h2, m2, p2,))

def minute_diff(h1: int, m1: int, p1: str, h2: int, m2: int, p2: str) -> int:
    
    # เช็คเงื่อนไขว่า ชั่วโมง เป็น 12 มั้ย ถ้าใช่ ให้เอา 12 ไปลบ เพื่อ คืนค่าเวลาให้กลับไปเป็นปกติ เช่น 00 (เที่ยงวัน) หรือ 12 (เที่ยงวัน) 
    if h1 == 12:
        h1 = h1 - 12
    if h2 == 12:
        h2 = h2 - 12

    # เช็คเงื่อนไขว่า ถ้า เป็น PM มั้ย ถ้าใช่ ให้เอา 12 ไปบวก เพื่อให้เวลากลับไปเป็นปกติ เช่น 00.00 - 23.00
    if p1 == "PM":
        h1 = h1 + 12
    if p2 == "PM":
        h2 = h2 + 12


    diff = abs(((h1 * 60) + m1) - ((h2 * 60) + m2))
    return diff


if __name__ == '__main__':
    main()
    


