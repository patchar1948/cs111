#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW08_2
# 204111 Sec 003

def main():
    test_skip_list()


def skip_list(word: str, start = 0, nemo = []) -> list[str]:
    # print(word)
    # Base Case
    if len(word) == len(nemo):
        return nemo

    # Divide & Conquer
    head = [word[start::start + 1]]
    nemo = nemo + head


    # Commbine
    return skip_list(word, start + 1, nemo)


def test_skip_list():
    print(skip_list("hello!"))
    assert skip_list("ABCD") == ['ABCD', 'BD', 'C', 'D']
    assert skip_list("hello!") == ['hello!', 'el!', 'l!', 'l', 'o', '!']
    assert skip_list("a") == ['a']
    print("Let's go to sleep")

if __name__ == '__main__':
    main()