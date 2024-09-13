#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW06_1
# 204111 Sec 003

def main():
#     line = str(input(""))
#     print(uniform(line))
    test_uniform()

    # print(uniform('vf,vc,v/,SDDFFF,</,/,vdm'))
    # print(line)

def uniform(line: str) -> str:
    
    num_low = list(filter(lambda x:str(x).islower(), list(line)))   # เช็คว่ามีตัวอักษรแต่ละตัวเป็นพิมพ์เล็กอะไรบ้าง
    num_low = len(num_low)                                          # เช็คว่ามีตัวอักษรแต่ละตัวเป็นพิมพ์เล็กกี่ตัว
    # print(num_low)

    num_up = list(filter(lambda x:str(x).isupper(), list(line)))    # เช็คว่ามีตัวอักษรแต่ละตัวเป็นพิมพ์ใหญ่อะไรบ้าง  
    num_up = len(num_up)                                            # เช็คว่ามีตัวอักษรแต่ละตัวเป็นพิมพ์ใหญ่กี่ตัว
    # print(num_up)

    if num_low == num_up:                                           # ถ้าจำนวนตัวอักษรพิมพ์เล็ก = จำนวนตัวอักษรพิมพ์ใหญ่
        if line[0].islower():                                       # ถ้าอักษรตัวแรกเป็นพิมพ์เล็กให้อักษรททุกตัวเป็นพิมพ์เล็ก
            return line.lower()                                     # ให้ line นั้นเป็นพิมพ์เล็กทั้งหมด
        else:
            return line.upper()                                     # นอกเหนือจากนั้นให้ line นั้นเป็นพิมพ์ใหญ่ทั้งหมด

    elif num_low > num_up:                                          # ถ้าจำนวนตัวอักษรพิมพ์เล็ก > จำนวนตัวอักษรพิมพ์ใหญ่                                          
        return line.lower()                                         # ให้ line นั้นเป็นพิมพ์เล็กทั้งหมด

    else:
        return line.upper()                                         # นอกเหนือจากนั้นให้ line นั้นเป็นพิมพ์ใหญ่ทั้งหมด



def test_uniform():
    assert uniform('HaPpY') == 'HAPPY'
    assert uniform('cOdINg') == 'coding'
    assert uniform('coMP scI!!!') == 'comp sci!!!'
    print('all ok')



if __name__ == '__main__':
    main()