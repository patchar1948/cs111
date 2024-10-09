#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW14_2
# 204111 Sec 003

def main():
    list_x = [3, 7, 4, 9, 5, 2, 6]
    bottom_up_m_sort(list_x, True)
    print('--------')
    print(list_x)
    print('========')
    list_x = [3, 7, 4, 9, 5, 2, 6, 1]
    bottom_up_m_sort(list_x)
    print('--------')
    print(list_x)
    

def merge_sort(list_a: list[int], list_b: list[int]) -> list[int]:
    l_a = len(list_a)
    l_b = len(list_b)
    list_c = []
    i = 0
    j = 0
    while i < l_a and j < l_b:
        if list_a[i] < list_b[j]:
            list_c += [list_a[i]]
            i += 1
        else:
            list_c += [list_b[j]]
            j += 1
    if i < l_a:
        list_c += list_a[i:]
    if j < l_b:
        list_c += list_b[j:]
    return list_c 

def bottom_up_m_sort(list_x: list[int], show_steps: bool=False) -> None:
    list_b = list(map(lambda x: [x], list_x[:]))
    if show_steps is True:
        print(list_b)
    while len(list_b) > 1:
        list_c = []
        
        for i in range(0,len(list_b)-1,2):
            list_c.append(merge_sort(list_b[i], list_b[i + 1]))
        i += 2
        if i < len(list_b):
            list_c += [list_b[-1]]

        list_b = list_c
        if show_steps is True:
            print(list_b)
    list_x[:] = list_b[0]
    
    # return None

if __name__ == '__main__':
    main()