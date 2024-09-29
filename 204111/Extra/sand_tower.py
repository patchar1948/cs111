#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Extra_13
# 204111 sec 003

('''

        |>>~
        |
      /^^^\
     /     \
    /^^^^^^^\
   /         \
  /           \
 /             \
/:::::::::::::::\
''')

('''

                   |>>~ 
                   |
                 /^^^\ 
                /     \ 
               /^^^^^^^\
              /         \
   /^^^\     /           \
  /     \   /             \
 /^^^^^^^\ /               \
/::::::::/ :::::::::::::::::\
''')

def main():
    print(sand_towers([8, 8, 8, 8]))
    print(sand_towers([5, 8, 6, 8]))
    print(sand_towers([7, 6, 8, 8]))
    print(sand_towers([6, 7, 8, 8]))
    print(sand_towers([8, 7, 6, 8]))

def sand_towers(list_a: list[int]) -> str:
    # หาความสูงที่สูงที่สุด
    max_height = max(list_a)
    # จำนวนที่ต้องสร้าง sand tower
    num_towers = len(list_a) 

    # สร้าง list ว่างไว้ตามจำนวนสูงสุด
    result = []
    for i in range(max_height + 2):
        l_b = ' '
        result += [l_b]

    # สร้างปราสาท
    for i in list_a:
        # สร้างส่วนบนของปราสาท
        index = 0
        if i == max_height:
            result[0] += (i * ' ') + '|>>~' + ((i - 3) * ' ')
            result[1] += (i * ' ') + '|' + ((i) * ' ')
            index = 2
        else:
            for index in range(max_height - i + 2):
                result[index] += (i*2 + 1) * ' '
            index += 1
        # สร้าง 3 บรรทัดแรก
        result[index] += (((i - 2) * ' ') + '/^^^\\' + ((i - 2) * ' '))
        result[index + 1] += (((i - 3) * ' ') + '/     \\' + ((i - 3) * ' '))
        result[index + 2] += (((i - 4) * ' ') + '/^^^^^^^\\' +((i - 4) * ' '))

        index += 3

        # สร้าางตัวปราสาท (ตั้งแต่บรรทัดที่ 4)
        for j in range(4, i):
            result[index] += ((i - (j + 1)) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((i - (j + 1)) * ' ')
            index += 1

        # สร้างฐานปราสาท
        result[index] += ('/' + (((2 * i)) * ':'))

    # ประกอบปราสาท
    result[-1] = result[-1].strip(' ') + ':\\'
    result = '\n' + '\n'.join(result)
    return result
    
if __name__ == '__main__':
    main()