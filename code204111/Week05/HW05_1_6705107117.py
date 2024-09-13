#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW05_2
# 204111 Sec 003

def main():
    test_substitute_once()

def  substitute_once(text: str, old: str, new: str) -> str:
    position = text.find(old)                                           # หาตำแหน่งของตัวอักษรเก่าใน text
    if len(old) == 0:                                                   # ถ้าจำนวน old = 0                                                  
        New_text = text                                                 # คำใหม่ ก็คือคำเดิม
    elif position == -1:                                                # ถ้าจำนวน old = -1 (หาตัวอักษรไม่เจอใน text)
        New_text = text                                                 # คำใหม่ ก็คือคำเดิม
    else:
       New_text = text[:position ] + new + text[position + len(old):]
       # คำใหม่ ตัวอักษรตั้งแต่เริ่มต้นถึงตำแหน่งที่มี old + ตัวใหม่ + (ตำแหน่งที่มีตัวอักษรเดิม + จำนวนคำ ในคำที่ต้องการเปลี่ยน)เป็นต้นไป  

    # print(position)
    # print(New_text)
    return New_text


def test_substitute_once():
    assert substitute_once("battle","b","c") == "cattle"
    assert substitute_once("Bidding","i","u") == "Budding"
    assert substitute_once("doesn't","n't"," not") == "does not"
    assert substitute_once("ab","b","bbb") == "abbb"
    assert substitute_once("  ","","=") == "  "
    assert substitute_once('baaaaaab','aaa','c') == 'bcaaab'
    assert substitute_once('baaaaaab','d','c') == 'baaaaaab'
    print("all ok")

if __name__ == '__main__':
    main()