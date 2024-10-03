#!/usr/bin/env python3
#Patcharin
# 670510717
# Sec003

def main():
    # print(wet_area(3, 3, 1, [(1, 1)]))
    # wet_area(3, 3, 1, [(1, 1)])
    print(wet_area(4, 5, 1, [(1, 0), (2, 0), (3, 2)]))


def wet_area(m: int, n: int, v: int, sprinkler_list: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    l_a = []
    for i in range(m):
        l_b = []
        for j in range(n):
            l_b += [0]
        l_a += [l_b]

    for i in sprinkler_list:
        x = i[0]
        y = i[1]
        l_a[x][y] = 1
    # print(l_a)

    dict_ = dict()
    m_i = [1, 0, -1, 0]
    m_j = [0, 1, 0, -1]
    count_w = 0
    # m_i = [1, -1, -1, 1]
    # m_j = [1, 1, -1, -1]
    for k in range(m):
        for i in range(m):
            for j in range(n):
                if l_a[i][j] != 0:
                    continue
                
                if l_a[i][j] == 1:
                    count_w += 1
        dict_[(i,j)] = count_w
    return dict_

if __name__ == '__main__':
    main()