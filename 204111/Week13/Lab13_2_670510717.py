#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab13_2
# 204111 sec 003

def main():
    print(square_matrix([[2, 3, 4], [1, 2, 3]]))
    print(square_matrix([[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]]))


def square_matrix(list_x: list[list[int]]):
    max_row = len(list_x)
    max_column = max(len(x) for x in list_x)
    maxy = max(max_row, max_column)
    # print(maxy)
    for i in range(maxy):
        while len(list_x) < maxy:
            list_x.append([0]) # เติมแถว
        while len(list_x[i]) < maxy:
            list_x[i].append(0 * (maxy)) # เติมหลัก
        # list_x[i].append(0 * (maxy - len(list_x[i])))
    # print(list_x)

if __name__ == '__main__':
    main()
    # print(l_a)