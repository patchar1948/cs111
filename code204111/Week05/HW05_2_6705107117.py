#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW05_2
# 204111 Sec 003


def main():
    test_roman_numeral()

def roman_numeral(n: int) -> str:

    thousand = n // 1000
    hundred = (n % 1000) // 100
    ten = ((n % 1000) % 100) // 10
    digit = (((n % 1000) % 100) % 10)
    # print(thousand, hundred, ten, digit)
    roman1 = ""
    roman2 = ""
    roman3 = ""
    roman4 = ""

    if n == 0:
        return ""
    if digit == 1:
        roman1 = "I"
    if digit == 2:
        roman1 = "II"
    if digit == 3:
        roman1 = "III"
    if digit == 4:
        roman1 = "IV"
    if digit == 5:
        roman1 = "V"
    if digit == 6:
        roman1 = "VI"
    if digit == 7:
        roman1 = "VII"
    if digit == 8:
        roman1 = "VIII"
    if digit == 9:
        roman1 = "IX"

    if ten == 1:
        roman2 = "X"
    if ten == 2:
        roman2 = "XX"
    if ten == 3:
        roman2 = "XXX"
    if ten == 4:
        roman2 = "XL"
    if ten == 5:
        roman2 = "L"
    if ten == 6:
        roman2 = "LX"
    if ten == 7:
        roman2 = "LXX"
    if ten == 8:
        roman2 = "LXXX"
    if ten == 9:
        roman2 = "XC"

    if hundred == 1:
        roman3 = "C"
    if hundred == 2:
        roman3 = "CC"
    if hundred == 3:
        roman3 = "CCC"
    if hundred == 4:
        roman3 = "CD"
    if hundred == 5:
        roman3 = "D"
    if hundred == 6:
        roman3 = "DC"
    if hundred == 7:
        roman3 = "DCC"
    if hundred == 8:
        roman3 = "DCCC"
    if hundred == 9:
        roman3 = "CM"

    if thousand == 1:
        roman4 = "M"
    if thousand == 2:
        roman4 = "MM"
    if thousand == 3:
        roman4 = "MMM"
    if thousand == 4:
        roman4 = "MMMM"

    sum_roman_numeral = roman4 + roman3 + roman2 + roman1
    # print(sum_roman_numeral)
    return sum_roman_numeral



def test_roman_numeral():
    assert roman_numeral(0) == ""
    assert roman_numeral(4) == "IV"
    assert roman_numeral(9) == "IX"
    assert roman_numeral(25) == "XXV"
    assert roman_numeral(267) == "CCLXVII"
    assert roman_numeral(339) == "CCCXXXIX"
    assert roman_numeral(4999) == "MMMMCMXCIX"
    assert roman_numeral(4567) == "MMMMDLXVII"
    assert roman_numeral(123) == "CXXIII"
    assert roman_numeral(2) == "II"
    assert roman_numeral(3999) == "MMMCMXCIX"
    assert roman_numeral(567) == "DLXVII"
    assert roman_numeral(1) == "I"
    assert roman_numeral(836) == "DCCCXXXVI"
    assert roman_numeral(65) == "LXV"
    assert roman_numeral(19) == "XIX"
    # print(roman_numeral(4001))
    # for i in range(1, 5000):
    #     print(roman_numeral(i))

    print("all ok!")


if __name__ == '__main__':
    main()