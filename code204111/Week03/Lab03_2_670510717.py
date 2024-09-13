#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab03_2
# 204111 Sec 003

import math
def main():
    x = float(input("Input side length:")) # ใส่ค่า x เพื่อเอาไปหาด้านตรงข้ามมุมฉากในสูตรพีทาโกรัส
    print(f"area:{rectangle_area(x):.2f}")
    #test_rectangle_area()

def rectangle_area(x: float) -> float:
    side_square = ((5**0.5)*x*2)/7 # หาด้าน 1 ด้านของสี่เหลี่ยมจัตุรัส
    area_square = side_square**2

    return(area_square)

#def test_rectangle_area():
    #assert math.isclose(rectangle_area(5), 10.20, rel_tol=10**-2)
    #assert math.isclose(rectangle_area(6.5), 17.24, rel_tol=10**-2)
    #assert math.isclose(rectangle_area(9.3), 35.30, rel_tol=10**-2)
    #print("All OK!")


if __name__ == '__main__':
    main()

# ใช้สูตรพีทาโกรัสหาด้านตรงข้ามมุมฉาก(BC)จากสามเหลี่ยมABC
# สร้างจุด D E บนด้าน BC ตามลำดับ
# ใช้สามเหลี่ยมคล้ายเพื่อเทียบหาความยาว BD และ EC
# กำหนดให้ด้าน 1 ด้านในสี่เหลี่ยมแทนด้วย side_square
# side_square หาได้จาก sqrt(5)*x ลบกับ ด้าน BD และ EC
# หาพื้นที่สี่เหลี่ยมจาก side_square ยกกำลัง 2
