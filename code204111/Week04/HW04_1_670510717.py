#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW04_1
# 204111 sec 003

def main():
    # p = int(input("Pidgey:"))
    # c = int(input("Candy:"))

    test_calculate_exp()

def calculate_exp(p: int, c: int) -> int:
    # ถ้าจำนวน pidgey = 0 ค่า exp = 0 เสมอ
    if p == 0:
        return 0
        # print("EXP:", exp)

    # ถ้าจำนวน pidgey + candy >= 13 ที่เป็น 13 เพราะ ให้เลขที่ออกมาจากสมการไม่ติดลบ
    if (c + p >= 13):

        sum_ = (((c + p) - 13) // 11) + 1 # จำนวนรอบสูงสุดที่ evolve ได้ ที่ + 1 เพราะว่าบวกครั้งแรกที่ evolve ได้
        if sum_ <= p:
            return (sum_) * 1000
            # print("EXP:", exp)
        if sum_ > p: # ถ้าจำนวน รอบที่สามารถ evolve > pidgey ค่า exp ที่ได้จะขึ้นอยู่กับจำนวน pidgey สูงสุดที่มี
            return p * 1000
            # print("EXP:", exp)
    
    else:  
        return 0
            
def test_calculate_exp():
    assert calculate_exp(0, 12) == 0
    assert calculate_exp(1, 5) == 0
    assert calculate_exp(1, 12) == 1000
    assert calculate_exp(2, 12) == 1000
    assert calculate_exp(1, 120) == 1000
    assert calculate_exp(2, 22) == 2000
    assert calculate_exp(57, 0) == 5000
    assert calculate_exp(120, 0) == 10000
    assert calculate_exp(2, 24) == 2000
    assert calculate_exp(2, 22) == 2000
    assert calculate_exp(1, 11) == 0
    assert calculate_exp(1, 0) == 0
    assert calculate_exp(5,55) == 5000
    assert calculate_exp(0,32) == 0
    assert calculate_exp(55,5) == 5000
    assert calculate_exp(1200,0) == 108000
    assert calculate_exp(11,12) == 1000
    assert calculate_exp(2,12) == 1000
    assert calculate_exp(1,12) == 1000
    assert calculate_exp(2,22) == 2000
    assert calculate_exp(2,100) == 2000
    assert calculate_exp(5,51) == 4000
    
    print("all ok")

if __name__ == "__main__":
    main()