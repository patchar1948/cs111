#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

def lucky_name(name: str) -> bool:
    name = name.lower()
    front = name[0]
    back = name[-1]
    vowels = ["a", "e", "i", "o", "u"]

    if front in vowels:
        if not back in vowels:
            return True
        else:
            return False
    else:
        if back in vowels:
            return True
        else:
            return False


if __name__ == '__main__':
    assert lucky_name('Eric') is True
    assert lucky_name('Tony') is False
    assert lucky_name('Bruce') is True
    assert lucky_name('Eva') is False
    print('All OK!!')
