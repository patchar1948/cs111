#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab07_1
# 204111 Sec 003

'''
n = 4

    1 2 3 4
    2 2 3 4
    3 3 3 4
    4 4 4 4

'''
def main():
    n = int(input("n:"))
    print(corner_frame(n))
    


def corner_frame(n: int) -> str: #(n >= 2)
    ranger = list(range(1 ,n + 1))
    # print(ranger) -> [1, 2, 3, 4]

    line = list(map(lambda x:str((ranger[x-1:x] * x) + (ranger[x:])), ranger))
    # -> [1 - 1:1] + [1:]
    # -> [] + [1, 2, 3, 4]
    # -> [1, 2, 3, 4]

    line_1 = list(map(lambda x:x.strip('[]'), line))
    # -> 1, 2, 3, 4
    # print(line_1)

    corner_frame = '\n'.join(line_1).replace(',', '')
    # -> 1 2 3 4
    return corner_frame + '\n'

    # ถ้า n = 1-9 ผลลัพท์ จะออกมาเป็น สี่เหลี่ยมจัตตุรัส
    # ถ้า n > ผลลัพท์ จะไม่ออกมาเป็น สี่เหลี่ยมจัตตุรัส   

if __name__ == '__main__':
    main()