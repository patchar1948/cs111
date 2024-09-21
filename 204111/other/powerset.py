def powerset(set_a: set[int]) -> list[set[int]]:
    # powerset
    a = [set()]
    # want [set(), {2}, {1}, {1, 2}]
    with_2  = []
    for i in set_a:
        with_2 = list(map(lambda x: x | {i}, a))
        a += with_2

    # if DEBUG:
    #     print(a)
    # return a


    print(sorted(a))
    # want [set(), {2}, {1}, {1, 2}]


if __name__ == '__main__':
    powerset({1, 2, 3, 4})