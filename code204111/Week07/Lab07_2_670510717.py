#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab07_2
# 204111 Sec 003


def main():
#     n = int(input("n:"))
#     sep = str(input("sep:"))
    square_frame(50,'.')
    # square_frame(4,'.')



def  square_frame(n: int, sep: str=' ') -> str: # (n ≥ 3)
    

    ranger = list(range(0,n - 2)) # สร้าง list(range) ซ้ายขวา
    # print(ranger)

    rangee = list(range(0,n)) # สร้าง list(range) หัวท้าย
    # print(rangee)

    front = list(map(lambda y: (((n**2) - (n - 2)**2) - y), ranger))
    # print(front)
    max_ = len(str(max(front)))
    front = list(map(lambda x:str(x).zfill(max_), front))
    # print(front)

    up = list(range(1,n + 1))
    up = list(map(lambda x:str(x).zfill(max_), up))
    up = sep.join(up)
    print(up)

    back = list(map(lambda y: n + 1 + y, ranger))
    back = list(map(lambda x:str(x).zfill(max_), back))
    # print(back)

    # middle = str(list((max_ * (n - 2)) * sep) + ((n - 1) * sep))
    middle = (((max_ * (n - 2)) * sep) + ((n - 1) * sep))
    # print(middle)
    # middle = middle.replace(', ','').replace("'","").strip('[]')
    middle = list(map(lambda x: str(front[x]) + middle + back[x], ranger))
    middle = '\n'.join(middle)
    print(middle)

    bottom = list(map(lambda y:str((((n**2) - (n - 2)**2) - y - (n - 2))), rangee))
    bottom = list(map(lambda x:str(x).zfill(max_), bottom))
    bottom = sep.join(bottom)
    print(bottom)

if __name__ == '__main__':
    main()