#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

def generate_p_triple(m: int, n: int) -> None:
    a = (m**2) - (n ** 2)
    b = 2 * m * n
    c = (m**2) + (n ** 2)
    print(f'{a} {b} {c}')


if __name__ == '__main__':
    generate_p_triple(2, 1)
    generate_p_triple(3, 2)