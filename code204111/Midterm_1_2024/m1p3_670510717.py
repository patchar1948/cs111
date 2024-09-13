#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

def count_lucky_num(start: int, stop: int) -> int:
    ranger = list(range(start, stop))
    l_mod_7 = list(filter(lambda x: x % 7 == 0, ranger))
    l_have_not_7 = (list(filter(lambda x: not "7" in str(x), l_mod_7)))
    return len(l_have_not_7)


if __name__ == '__main__':
    assert count_lucky_num(1, 14) == 0
    assert count_lucky_num(1, 15) == 1
    assert count_lucky_num(14, 22) == 2
    print('All OK!!')
