#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW13_3
# 204111 sec 003

def main():
    print(sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3],
[3, -1, -1, 2, 0, -1, 2, 1],
[3, 0, 1, 2, 3, 1, 3, 1],
[2, 2, 1, -1, -1, 2, 0, 3],
[1, 3, 2, 1, 3, 2, 2, 1],
[1, 2, 2, 1, 3, 3, 1, 3],
[2, 2, 2, 2, 2, 2, 3, 3],
[1, 3, 2, 3, 1, 1, 2, 2]]))

# def sum_d_product(m: list[list[int]]) -> int:

def sum_d_product(m: list[list[int]]) -> int:
    if len(m) == 2 and len(m[0]) == 2 and len(m[1]) == 2:
        num = (m[0][0] * m[1][1]) + (m[0][1] * m[1][0])
        # print(num)
        return num
    else:
        n = len(m)
        up = m[:n // 2] # [[1, 2, 3, 4], [1, 2, 3, 4]]
        down = m[n// 2:]
        left_up = list(map(lambda x: up[x][:n // 2], range(len(up))))
        right_up = list(map(lambda x: up[x][n // 2:], range(len(up))))
        left_down = list(map(lambda x: down[x][:n // 2], range(len(down))))
        right_down = list(map(lambda x: down[x][n // 2:], range(len(down))))

        return sum_d_product([[sum_d_product(left_up), sum_d_product(right_up)], [sum_d_product(left_down), sum_d_product(right_down)]])







if __name__ == '__main__':
    main()

# for i in m:
#     l = list(map(lambda x: i[x:], range(0, len(i), len(i) // 2)))
#     print(l)


# -----------------------------------------------------------------------------
# n = len(list_m)
#         l = []
#         for i in range(0, n, 2):
#             print(list_m)
#             print(i)
            
            # for j in range(0, n, 2):
            #     l += [[list_m[i][j], list_m[i][j + 1]], [list_m[j + 1][i], list_m[j + 1][i + 1]]]
            #     i = 0
            #     j = 0
        # print(l)