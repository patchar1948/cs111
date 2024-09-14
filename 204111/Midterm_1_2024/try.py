def main():
    test1()

def help_find_mode(score_list, start = 0, list_a = []):

    if len(score_list) == len(list_a):
        print([])
        return []
    if start >= len(score_list):
        print(list_a)
        return list_a

    head = score_list[start]
    n = score_list.count(head)
    list_a.append([head,n])
    start = start + n

    return help_find_mode(score_list, start, list_a )


def test1():
    # assert help_find_mode([100, 50, 50, 80, 70]) == [50] 
    assert help_find_mode([30, 20, 30, 20, 20, 100, 50, 100, 100]) == [20, 100] 
    assert help_find_mode([-20, 50, 50, 80, 70, -20]) == [-20, 50] 
    assert help_find_mode([40, 20, 30, 10]) == [10, 20, 30, 40] 
    print("ALL OK!")

if __name__ == '__main__':
    main()