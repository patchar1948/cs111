#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab04_2
# 204111 sec 003
# TA P'Ta


def main():
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    my_min_mid_max(a, b, c)
    
    

def my_min_mid_max(a: int, b: int, c: int) -> None:
    
    if a < b:
        min_ = a
        max_ = b 

    else: 
        min_ = b
        max_ = a
# นำค่า  c ไปเปรียบเทียบกับค่า min_ 
    if c <= min_:
        mid_ = min_ # ถ้าค่า min_ มากกว่า c จะได้ว่า ค่า mid_ = ค่า min_
        min_ = c
    
    if c >= max_:
        mid_ = max_ # ถ้าค่า c มากกว่า max_ จะได้ว่า ค่า mid_ = ค่า max_
        max_ = c
    if c > min_ and c < max_:
        mid_ = c




    print("min =", min_)

    print("mid =", mid_)

    print("max =", max_)

    
    
if __name__ == '__main__':
    main()