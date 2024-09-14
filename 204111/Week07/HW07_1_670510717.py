#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW07_1
# 204111 Sec 003


def main():

    # print_polynomial([(2, -6), (0, -8), (1, 34)], 'x')
    # print("-----------------------------------------------------")
    # print_polynomial([(2,6),(0,10)], 'x')
    # transfer()
    test_print_polynomial()

def  print_polynomial(pc_list: list[tuple[int, float]], v: str) -> str:
    l_b = sorted(pc_list, key= lambda x: x[0], reverse = True)
    a = list(range(len(l_b)))
    l_a = list(filter(lambda x:x[1] != 0,l_b))
    b = list(range(len(l_a)))

    power_and_confficient = list(map(lambda x: transfer(l_a[x][0], l_a[x][1], v), b))

    if power_and_confficient[0][0] == '-': power_and_confficient[0] = power_and_confficient[0].replace(" ", "")

    else: power_and_confficient[0] = power_and_confficient[0].replace("+ ","")

    result = ' '.join(power_and_confficient)
    return(result)

def transfer(power,coef, v):
    # confficient = 0
    if coef == 0:return ''
    # confficient = 1
    if coef == 1:
        if power == 0:return '+ ' + str(coef)
        if power == 1:return '+ ' + v
        if power >= 2:return '+ ' + v + '^' + str(power)
    # confficient = -1
    if coef == -1:
        if power == 0:return '- ' + str(coef)[1:]
        if power == 1:return '- ' + v
        if power >= 2:return '- ' + v + '^' + str(power)
    # confficient > 2
    if coef > 0:
        if power == 0:return '+ ' + str(coef)
        if power == 1:return '+ ' + str(coef) + v
        if power >= 2:return '+ ' + str(coef) + v + '^' + str(power)
    # confficient < -2
    if coef < 0:
        if power == 0:return '- ' + str(coef)[1:]
        if power == 1:return '- ' + str(coef)[1:] + v
        if power >= 2:return '- ' + str(coef)[1:] + v + '^' + str(power)

def test_print_polynomial():
    assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'x') == '-6x^2 + 34x - 8' 
    assert print_polynomial([(2, -6), (0, -8), (1, 34)], 'y') =='-6y^2 + 34y - 8'
    assert print_polynomial([(0,0), (1,2.33)], 'x') == '2.33x'
    assert print_polynomial([(2, -66), (0, -8), (1, 34)],"x")=='-66x^2 + 34x - 8'
    assert print_polynomial([(2, 6), (0, -8), (1, 34)],"y")=='6y^2 + 34y - 8'
    assert print_polynomial([(2, -6), (0, -1), (1, 34)],"x")=='-6x^2 + 34x - 1'
    assert print_polynomial([(2, -6), (0, 1), (1, 34)],"x")=='-6x^2 + 34x + 1'
    assert print_polynomial([(2, 6), (0, 0), (1, 0)],"x")=='6x^2'
    assert print_polynomial([(2, 0), (0, -1), (1, 0)],"x")=='-1'
    assert print_polynomial([(5, 2), (4, -2), (1, 0)],"x")=='2x^5 - 2x^4'
    assert print_polynomial([(5, 1), (4, -1), (0, 1)],"x")=='x^5 - x^4 + 1'
    assert print_polynomial([(0, 1), (1, 1)],"x")=='x + 1'
    assert print_polynomial([(0, 1), (1, -1)],"x")=='-x + 1'
    assert print_polynomial([(1, 0), (0 , -2)],"x")=='-2'
    assert print_polynomial([(2, -100000), (1 , -1),(0 , -1),(3 , -1)],"x")=='-x^3 - 100000x^2 - x - 1'
    assert print_polynomial([(1, 0.0001),(2,0)], "x") == '0.0001x'
    # assert print_polynomial([(0, 0)],"x")== "0"
    print("ok")



if __name__ == '__main__':
    main()