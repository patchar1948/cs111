#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW11_1
# 204111 Sec 003

def main():
    pass

def words_to_num(words: str) -> int:
    unit_ = {"" : 0, "one": 1, "two" : 2, "three" : 3, "four" : 4, "five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}
    ten_list = {"": 0, "": 0, "twenty": 20 , "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": , "eighty": 80, "ninety": 90, "hundred": 100}