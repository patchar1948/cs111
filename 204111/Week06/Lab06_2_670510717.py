#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab06_2
# 204111 Sec 003

def main():
    list_a = [1, 2, 3, 4]
    dest_rotate_list(list_a, -7)
    print(list_a)

    # test_dest_rotate_list()


def  dest_rotate_list(list_a: list[int], n: int) -> None:
    if abs(n) > len(list_a):                                # ถ้าค่าของ n มีค่ามากกว่า ค่าของตำแหน่งใส่ list_a
        n = n % len(list_a)                                 # ให้ใช้ค่า n ที่หาจากสูตร 

    list_a[:] = list_a[-n :] + list_a[:-n]                  # หมุนด้วนตำแหน่งที่ -n ถึงตำแหน่งที่ -n
    # list_[:] คือ การเคลียร์ค่าของ list_a ให้เป็นลิสว่าง
    
    # return list_a



# def test_dest_rotate_list():
#     list_a = [1, 2, 3, 4]
#     dest_rotate_list(list_a, 1)
#     assert list_a == [4, 1, 2, 3]



if __name__ == '__main__':
    main()