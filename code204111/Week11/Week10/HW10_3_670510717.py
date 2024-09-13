#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW10_3
# 204111 Sec 003


def polynomial_addition(
        p1: list[tuple[int, float]], 
        p2: list[tuple[int, float]],
    ) -> list[tuple[int, float]]:
    
    p1, p2 = sorted(p1, reverse = True), sorted(p2, reverse = True)
    i = j = 0
    result = []

    while i < len(p1) and j < len(p2):
        if p1[i][0] == p2[j][0]:
            sum_ = (p1[i][1] + p2[j][1])
            if sum_ != 0:
                result = result + [(p1[i][0], sum_)] # [r] = [r] + [(a,b)]
            i += 1
            j += 1
        else:
            # p1 > p2
            if  p1[i][0] > p2[j][0]:
                result = result + [(p1[i][0], p1[i][1])]
                i = i + 1

            else:
                p1[i][0] < p2[j][0]
                result = result + [(p2[j][0], p2[j][1])]
                j = j + 1
    if i < len(p1):
        result = result + p1[i:]
    if j < len(p2):
        result = result + p2[j:]

    return result


def test():
    expected = [(1, 35), (0, -6)]
    got = polynomial_addition([(2, 6), (1, 34), (0, -8)], [(2, -6), (0, 2), (1, 1)])
    assert expected == got, f"expected:={expected}, got:={got}"

    expected = [(3, -1), (2, 6), (1, 1), (0, 2)]
    got = polynomial_addition([(2, 6), (3, -1)], [(0, 2), (1, 1)])
    assert expected == got, f"expected:={expected}, got:={got}"

    # expected = [(0, 0.3)]
    # got = polynomial_addition([(0, 0.1+0.1)], [(0, 0.1)])
    # assert expected == got, f"expected:={expected}, got:={got}"
    print("pai tam meaow tor")

if __name__ == '__main__':
    test()
