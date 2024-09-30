#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab12_1
# 204111 Sec 003
def main():
    print(multiply_polynomials([2, 1, 3], [4, 5])) # ---> [8, 10, 12, 15]

def multiply_polynomials(p1: list[int], p2: list[int]) -> list[int]:
    p1 = p1[::-1]
    p2 = p2[::-1]
    list_p1 = list(map(lambda x, y: (x,y), p1, range(len(p1))))
    list_p2 = list(map(lambda x, y: (x,y), p2, range(len(p2))))
    # print(list_p1, list_p2)

    coef = []
    power = []
    dict_poly = dict()
    for i in range(len(list_p1)):
        for j in range(len(list_p2)):
            coef = list_p1[i][0] * list_p2[j][0]
            power = list_p1[i][1] + list_p2[j][1]
            if power in dict_poly:
                dict_poly[power] += coef
            else:
                dict_poly[power] = coef
    result = list(map(lambda x: x[1], dict_poly.items()))[::-1]
    # result = list(zip(coef, power))
    # result = list(filter(lambda x: x[0] != 0, result))
    # print(result)
    # result = sorted(result, key = lambda x: x[1], reverse = True)
    # result = list(map(lambda x: x[0], result))
    return result



if __name__ =='__main__':
    main()
