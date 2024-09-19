#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW12_3
# 204111 Sec 003
# [[0,0,0],[],[]]

def main():
    print(ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]))

def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    # สร้าง list แต่ละชั้น
    l_a = []
    for i in range(m):
        l_b = []
        for j in range(n):
            l_b += [0]
        l_a += [l_b]
    # print(l_a)
    for i in bomb_list:
        x = i[0]
        y = i[1]
        l_a[x][y] = 1
    # print(l_a)
    dict_ = {}
    m_i = [1, 1, 0, -1, -1, -1, 0, 1]
    m_j = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(m):
        for j in range(n):
            if l_a[i][j] != 0:
                continue
            count_b = 0
            for k in range(8):
                c_i = i + m_i[k]
                c_j = j + m_j[k]
                if c_i <= -1 or c_j <= -1:
                    continue
                if c_j >= n or c_i >= m:
                    continue
                if l_a[c_i][c_j] == 1:
                    count_b += 1
            if count_b != 0:
                dict_[(i, j)] = count_b
    # print(dict_)
    return dict_


if __name__ == '__main__':
    main()
