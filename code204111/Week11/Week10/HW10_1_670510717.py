#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW10_1
# 204111 Sec 003

def eratosthenes(n: int, show_step: bool=False, start = 2) -> list[int]:
    if n == 1:
        return []
    # if n == 2:
    #     return [2]
    ranger = list(range(2, n + 1))
    # list_result_2 = list(filter(lambda x: x % 2 != 0 or x == 2, ranger))

    while n ** (0.5) >= start:
        if start in ranger:
            list_result = list(filter(lambda x: x % start != 0 or x == start, ranger))
            if show_step == True:
                result =   '{}: {}'.format(str(start), list_result)
                print(result)

        ranger = list_result
        start = start + 1
    return ranger
if __name__ == '__main__':
    result = eratosthenes(20, True)
    print('----')
    print(result)