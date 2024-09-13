#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW07_3
# 204111 Sec 003


def main():
    test_num_to_word()
    # for i in range(0, 1000000000, 1000):
    #     print(num_to_word(i))

def three_digits_to_word(n: int) -> str:

    unit_list = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                    "sixteen", "seventeen", "eighteen", "nineteen"]

    ten_list = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]

    # แบ่งคิดตัวเลขในแต่ละหลัก
    a = n // 100
    ten_unit = n % 100
    b = (n % 100) // 10
    c = (n % 100) % 10

    # zero
    if n == 0:
        return "zero"
    # hundred
    if a == 0:
        hundred = ""
    if a >= 1 and a <= 9:
        hundred = unit_list[a] + " " + "hundred"

    # ten
    if ten_unit >= 0 and ten_unit <= 19:
        ten = unit_list[ten_unit]

    if ten_unit > 19 and ten_unit <= 99:
        if c == 0:
            ten = ten_list[b]
        else:
            ten = ten_list[b] + "-" + unit_list[c]

    ten = ' ' + ten

    word = (hundred + ten).strip(" ")

    # print(word)
    return word

def num_to_word(num: int) -> str:
    num = str(num)

    hundred_digit = (num[-3:])
    hundred = three_digits_to_word(int(hundred_digit))

    thousand_digit = num[-6:-3]
    if thousand_digit == '' or int(thousand_digit) == 0:
        thousand = ''
    else:
        thousand = three_digits_to_word(int(thousand_digit)) + ' thousand '

    # elif int(thousand_digit) != 0:


    million_digit = (num[-9:-6])
    if million_digit == '' or int(million_digit) == 0 :
        million = ''
    else:
        million = three_digits_to_word(int(million_digit)) + ' million '
    


    billion_digit = (num[-len(num):-9])
    if billion_digit == '' or int(billion_digit) == 0:
        billion = ''

    else:
        billion = three_digits_to_word(int(billion_digit)) + ' billion '

    if billion + million + thousand != '' and hundred == "zero":
        hundred = ''
        
    word = billion + million + thousand + hundred
    # print(word)
    return(word).strip(" ")


def test_three():
    assert three_digits_to_word(14) == "fourteen" 
    assert three_digits_to_word(248) == "two hundred forty-eight" 
    assert three_digits_to_word(111) == "one hundred eleven" 
    assert three_digits_to_word(0) == "zero"
    print("<3")

def test_num_to_word():
    assert num_to_word(14) == "fourteen" 
    assert num_to_word(248) == "two hundred forty-eight" 
    assert num_to_word(111) == "one hundred eleven" 
    assert num_to_word(0) == "zero"
    assert num_to_word(42641323862) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"
    assert num_to_word(1) == "one"
    assert num_to_word(10) == "ten"
    assert num_to_word(100) == "one hundred"
    assert num_to_word(1000) == "one thousand"
    assert num_to_word(10000) == "ten thousand"
    assert num_to_word(100000) == "one hundred thousand"
    assert num_to_word(1000000) == "one million"
    assert num_to_word(10000000) == "ten million"
    assert num_to_word(100000000) == "one hundred million"
    assert num_to_word(1000000000) == "one billion"
    assert num_to_word(10000000000) == "ten billion"
    assert num_to_word(100000000000) == "one hundred billion"
    print("<3")
if __name__ == '__main__':
    main()

# 1 == "one"
# 10 == "ten"
# 100 == "one hundred"
# 1000 == "one thousand"
# 10000 == "ten thousand"
# 100000 == "one hundred thousand"
# 1000000 == "one million"
# 10000000 == "ten million"
# 100000000 == "one hundred million"
# 1000000000 == "one billion"
# 10000000000 == "ten billion"
# 100000000000 == "one hundred billion"
