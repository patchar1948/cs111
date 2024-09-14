def main():
    test()

# def is_right_triangle1(a: int, b: int, c: int):
    # max_ = max(a, b, c)
    # min_ = min(a, b, c)
    # mid_ = (a + b + c) - (max_ + min_)
    # # print("Max:",max_, "Min:",min_, "Mid:",mid_)

    # if max_ ** 2 == (min_** 2) + (mid_**2):
    #     return True
    # else:
    #     return False

def is_right_triangle(a, b, c):
    if a**2 == (b**2) + (c**2) or b**2 == (a**2) + (c**2) or c**2 == (b**2) + (a**2):
        return True
    else:
        return False

def test():
    assert is_right_triangle(3, 4, 5) is True 
    assert is_right_triangle(5, 3, 4) is True 
    assert is_right_triangle(5, 12, 13) is True 
    assert is_right_triangle(5, 13, 13) is False 
    print(":)")

if __name__ == '__main__':
    main()