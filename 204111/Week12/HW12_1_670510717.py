#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW12_1
# 204111 Sec 003

def main():
    print(scramble("bee"))


def scramble(word: str) -> list[str]:

    result = [word[0]] # choose first word
    c_i = 1 # index เริ่มต้น
    while c_i < len(word): 
        temp = []
        for i in result:
            temp += (list(map(lambda x: i[:x] + word[c_i] + i[x:], range(c_i + 1))))
        result = list(set(temp))
        c_i += 1
    # result = list(set(result))
    return result
        # สร้าง temp ที่ copy result ขึ้นมา
        # เพิ่ม temp เข้าไปใน result
        # loop หยิบของจาก result
        # สร้าง range ที่มากกว่า len ของ result ในรอบนั้น
        # map insert ตัวอักษรด้วย range ที่สร้าง

if __name__ == '__main__':
    main()