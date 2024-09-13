#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab08_2
# 204111 Sec 003
def main():
    test_reverse_digits()

def reverse_digits(x: int) -> int:
    if x < 0:
        return reverse_digits_helper(x) * -1
    else:
        return reverse_digits_helper(x)

def reverse_digits_helper(x, div = None):
    x = abs(x)
    
    if div is None:
        div = 10**(len(str(x)) - 1)

    # Base Case
    if div <= 1:
        return x

    # Divide & Conquer
    head = x % div
    tail = div // 10

    # Combine
    return (reverse_digits_helper(head, tail) * 10) + (x // div)

def test_reverse_digits():
    # print(reverse_digits(5432))
    assert reverse_digits(1234) == 4321
    assert reverse_digits(1) == 1
    assert reverse_digits(45665) == 56654
    assert reverse_digits(1000) == 1
    assert reverse_digits(-1234) == -4321
    print("Let's go to sleep")

if __name__ == '__main__':
    main()