#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab13_1
# 204111 sec 003

def main():
    assert (matrix_mult([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]])) == [[58,64],[139,154]]
    assert (matrix_mult([[1,2,3],[4,5,6]],[[7,8,5,9,3],[9,10,-3,7,13],[11,12,6,2,9]])) == [[58, 64, 17, 29, 56],[139, 154, 41, 83, 131]]
    assert (matrix_mult([[48, 59]],[[31], [37], [30]])) == None
    assert (matrix_mult([[48, 59]],[[31], [37], [30, 3]])) == None
    assert (matrix_mult([[1,2,3,4]],[[5],[6],[7],[8]])) == [[70]]
    assert (matrix_mult([[1,0,2],[-1,3,1]],[[3,1],[2,1],[1,0]])) == [[5,1],[4,2]]
    assert (matrix_mult([[21], [19], [47], [33], [1]],[[63, 1, 65, 47, 18], [75, 29, 97, 96, 3]])) == None
    print("aaa")


def matrix_mult(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    for row in m1:
        if len(row) != len(m2):
            return None
    temp, result, sum_temp, c  = [], [], [], []
    # sum_temp = []
    # result = []
    # c = []

    for i in range(len(m1)):
        for j in range(len(m2[0])):    # ลูปตามจำนวนก้อน2
            for k in range(len(m2)):
                a = m1[i][k]* m2[k][j]
                temp += [a]
                # print(temp)
            sum_temp += [sum(temp)]
            temp = []
        c += [sum_temp]
        sum_temp = []
    result += c
    return result
        

if __name__ == '__main__':
    main()


