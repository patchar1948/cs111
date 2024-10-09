#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW14_3
# 204111 Sec 003

def main():
    list_x = \
    ['beer', 'wine', 'vinegar', 'vodka']
    radix_word(list_x, True)
    print('--------')
    print(list_x)
    print("========")
    list_x = \
    ['beer', 'wine', 'vinegar', 'vodka']
    radix_word(list_x)
    print('--------')
    print(list_x)
    pass

def radix_word(list_x: list[str], show_steps=False) -> None:
    maxxy = max(len(x) for x in list_x)
    # print(maxxy)
    list_a = list(map(lambda x: x + (' ' * (maxxy - len(x))), list_x))
    for index_ in range(maxxy-1, -1, -1):
        for i in range(1, len(list_a)):
            j = i
            while j > 0 and list_a[j][index_] < list_a[j - 1][index_]:
                list_a[j], list_a[j - 1] = list_a[j - 1], list_a[j]
                j -= 1
        if show_steps is True:
            list_b = list(map(lambda x: x.strip(), list_a))
            print(list_b)
    
    list_x[:] = list(map(lambda x: x.strip(), list_a))
        # print(list_x)
    
    # return None

if __name__ == '__main__':
    main()