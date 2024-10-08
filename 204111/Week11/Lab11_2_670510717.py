#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab11_2
# 204111 Sec 003

def main():
    test_matching_sum()


def matching_sum(t: tuple[int], target_value: int) -> tuple[int]:
    s = set()
    for i in t:
        num = target_value - i # นำ num ไปใช้ในการหา
        if num in s:
            # print([num, i])
            return [num, i] # return คำตอบ ที่เป็นคู่ที่ บวกกันแล้วเท่ากับ target_value
        else:
            s.add(i) # เพิ่ม i เข้าไปใน s
    return []

def test_matching_sum():
    # print(matching_sum((1,), 1))
    # print(matching_sum((1,2,1), 2))
    print(matching_sum((5, 2), 7))
    # print(matching_sum((10, -1, 1, -8, 3, 1), 2))
    # print(matching_sum((10, -1, 1, -8, 3, 1), 10))

    # print("Let's go to sleep")

if __name__ =='__main__':
    main()