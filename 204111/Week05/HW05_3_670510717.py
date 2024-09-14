#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW05_3
# 204111 Sec 003

def main():
    test_is_valid_license()
    test_is_valid_license_1()    


def is_valid_license(license_str: str) -> bool:

    if len(license_str) > 3 and len(license_str) <= 7: # ตัวอักขระที่อยู่บนป้ายทะเบียนต้อง 3 ตัวขึ้นไป แต่ไม่เกิน 7 ตัว
        alphabet = 0
        number = 0
        if license_str[0].isalpha():            # ถ้าตำแน่งที่ 0 เป็นตัวอักษร
            index = 2                           # เก็บค่า 2 ไปใช้ในการเช็คตำแน่งที่ 2 ต่อไป
            if license_str[1].isalpha():        # ถ้าตำแหน่งที่ 1 เป็นตัวอักษร
                alphabet = 1
            else:
                alphabet = 0
        else:
            index = 3                           # ถ้าตำแหน่งที่ 0 เป็นตัวเลข ให้เก็บค่า 3 เพื่อเอาไปคิดตำแหน่งที่ 3 ต่อ
            if license_str[1].isalpha() and license_str[2].isalpha(): # ถ้าตำแหน่งที่ 1 และ 2 เป็นตัวอักษร ให้เก็บค่า 1
                       
                alphabet = 1
            else:
                alphabet = 0

        if index == 2:                          # จากบรรทัดที่ 17 ถ้า index เท่ากับ 2

            if license_str[2:].isdigit() and len(license_str[2:]) <= 4: # ถ้าตำแน่งที่ 2 เป็นต้นไปเป็นตัวเลข และ ชุดตัวเลขไม่เกิน 4 ตัว
                number = 1                      # ให้เก็บค่า 1
            else:
                number = 0

        if index == 3:                          # จากบรรทัดที่ 23 ถ้า index เท่ากับ 2
            if license_str[3:].isdigit():       # ถ้าตำแน่งที่ 3 เป็นต้นไปเป็นตัวเลข
                number = 1                      # ให้เก็บค่า 1
            else:
                number = 0

        if alphabet + number == 2:              # alphabet + number เท่ากับ 2 ให้ประกาศว่า ถูกต้อง
            return True

        else:
            return False

    else:
        return False

# *******************************************************************************

def is_valid_license_1(license_str: str) -> bool:
    
    if len(license_str) < 3 and len(license_str) <= 7:
        return False

    alphabet = 0
    number = 0
    if license_str[0].isalpha():
        index = 2
        if license_str[1].isalpha():
            alphabet = 1
    else:
        index = 3
        if license_str[1].isalpha() and license_str[2].isalpha():
            alphabet = 1

    if license_str[index:].isdigit() and len(license_str[index:]) <= 4:
        number = 1

    if alphabet + number == 2:
        return True
    else:
        return False


def test_is_valid_license():
    assert is_valid_license("9AB8954") is True
    assert is_valid_license("9999") is False
    assert is_valid_license("CD700") is True
    assert is_valid_license("99D1234") is False
    assert is_valid_license("A") is False
    assert is_valid_license("A1") is False
    assert is_valid_license("AB12345") is False
    assert is_valid_license("9AB12345") is False
    print("all ok!")

def test_is_valid_license_1():
    assert is_valid_license_1("9AB8954") is True
    assert is_valid_license_1("9999") is False
    assert is_valid_license_1("CD700") is True
    assert is_valid_license_1("99D1234") is False
    assert is_valid_license_1("A") is False
    assert is_valid_license_1("A1") is False
    assert is_valid_license_1("AB12345") is False
    assert is_valid_license_1("9AB12345") is False
    print("all ok!")

if __name__ =="__main__":
    main()
