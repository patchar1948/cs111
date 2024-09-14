#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW11_1
# 204111 Sec 003

def main():
    test()

def words_to_num(words: str) -> int:
    # 0 - 99
    unit_num = {"zero" : 0, "one": 1, "two" : 2, "three" : 3, "four" : 4, "five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20 , 
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70 , "eighty": 80, "ninety": 90}
    
    large_num = {"hundred": 100 ,"thousand": 1000, "million": 1000000, "billion": 1000000000}
    
    # แบ่งเป็นแต่ละตัว
    words = words.split()
    temp = 0 # เก็บค่าที่เปลี่ยนแปลงไปเรื่อยๆ
    sum_num = 0 # total ผลรวมของค่า
    for i in words:
        if i in unit_num:
            temp += unit_num[i] # บวกค่าที่เจอใน temp
        elif "-" in i:
            word  = i.split("-")
            temp += unit_num[word[0]] + unit_num[word[1]]
        elif i == 'hundred':
            temp *= 100 # เพิ่ม 100 เข้า temp
        elif i in large_num:
            sum_num += temp * large_num[i] # บวกค่าที่เจอใน temp คูณด้วยตัวที่เจอ
            temp = 0 # เคลียร์ temp ทันที
    
    sum_num += temp

    return sum_num
    
def test():
    print(words_to_num("fourteen")) # 14
    print(words_to_num("two hundred forty-eight")) # 248
    print(words_to_num("one hundred eleven")) # 111
    print(words_to_num("five hundred fifty-two")) # 552
    print(words_to_num("three thousand four hundred fifty-two")) # 3452
    print(words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two")) # 42641323862
    print("Let's go to sleesp")

if __name__ == "__main__":
    main()