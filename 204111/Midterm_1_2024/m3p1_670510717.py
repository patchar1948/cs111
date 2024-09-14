def main():
    test()

def find_mode(score_list: list[int]) -> list[int]:
    score_list = sorted(score_list)
    a = help_find_mode(score_list,[])
    #print(a)
    a = sorted(a,key = lambda x: x[1],reverse = True)
    a = list(map(lambda x: x[0] if x[1] == a[0][1] else [], a))
    a = list(filter(lambda x: x != [],a))
    return a


def help_find_mode(score_list, list_a = [], start = 0):
    #print(score_list,list_a)
    # if len(score_list) == len(list_a):
    #     return []

    if start >= len(score_list):
        #print(list_a)
        return list_a

    head = score_list[start]
    n = score_list.count(head)
    list_a.append([head,n])
    start = start + n

    return help_find_mode(score_list, list_a, start)

def test():
    # print(find_mode([100, 50, 50, 80, 70]))
    assert find_mode([100, 50, 50, 80, 70]) == [50] 
    assert find_mode([30, 20, 30, 20, 20, 100, 50, 100, 100]) == [20, 100] 
    assert find_mode([-20, 50, 50, 80, 70, -20]) == [-20, 50] 
    assert find_mode([40, 20, 30, 10]) == [10, 20, 30, 40] 
    print("ALL OK!")


if __name__ == '__main__':
    main()