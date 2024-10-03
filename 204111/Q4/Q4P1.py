#!/usr/bin/env python3
#Patcharin
# 670510717
# Sec00
# DEBUG = False


def projections(n: int, opaque_cells: list[tuple[int]]) -> dict[str, list[list[int]]]:
    l_xy = []
    for i in range(n):
        l_b = []
        for j in range(n):
            l_b += [0]
        l_xy += [l_b]

    l_xz = []
    for i in range(n):
        l_b = []
        for j in range(n):
            l_b += [0]
        l_xz += [l_b]

    l_yz = []
    for i in range(n):
        l_b = []
        for j in range(n):
            l_b += [0]
        l_yz += [l_b]


    for i in opaque_cells:
        # print(i)
        x = i[0]
        y = i[1]
        z = i[2]
        l_xy[y][x] = 1
        l_xz[z][x] = 1
        l_yz[z][y] = 1

    # print(l_xy)
    # print('-------')
    # print(l_xz)
    # print('-------')
    # print(l_yz)

    key_ = ['xy', 'xz', 'yz']
    value_ = [l_xy, l_xz, l_yz]
    dict_ = dict(zip(key_, value_))

    # print(dict_)
    pretty_print_dict(dict_)
    return dict_





def pretty_print_dict(data: dict):
    print("{")
    for key, value in data.items():
        print(f'  "{key}": [')
        for row in value:
            print(f'    {row},')
        print("  ]")
    print("}")


if __name__ == '__main__':
    assert projections(4, [(0, 0, 0), (2, 1, 3)]) ==  {
    'xy': [[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],
    'xz': [[1, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]],
    'yz': [[1, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 1, 0, 0]]
    }

    print('ALL OK')
