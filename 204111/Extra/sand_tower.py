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
    print(sand_towers([7, 8, 6, 8]))
    # print(sand_towers([7, 6, 8, 8]))
    # print(sand_towers([6, 7, 8, 8]))
    # print(sand_towers([8, 7, 6, 8]))

def sand_towers(list_a: list[int]) -> str:
    # หาความสูงที่สูงที่สุด
    max_height = max(list_a)
    # จำนวนที่ต้องสร้าง sand tower
    # num_towers = len(list_a) 


    # สร้าง list ว่างไว้ตามจำนวนสูงสุด
    result = []
    for i in range(max_height + 2):
        l_b = ' '
        result += [l_b]
    
    # result[0] += "--"
    # print(result)
    for i in range(len(list_a)):
        # ก่อนสุดท้าย
        if i != len(list_a) - 1:
            # สร้างฐานปราสาท
            tail = ('/' + (((2 * list_a[i])) * ':'))
            # สร้างบรรทัดว่าง
            if list_a[i] < max_height:
                for k in range(max_height - list_a[i] + 2):
                    result[k] += ' ' * (len(tail) + 1)
                    # print(result)

                
            else:
                # สร้างธง
                flag = ''
                if list_a[i] == max_height:
                    result[0] += ((list_a[i]) * ' ') + '|>>~' + ((list_a[i] - 3) * ' ')
                    result[1] += (((list_a[i]) * ' ') + '|') + ((list_a[i]) * ' ')
                    k = 1

            # สร้างยอดปราสาท
            result[k+1] += (((list_a[i] - 2) * ' ') + '/^^^\\' + ((list_a[i] - 2) * ' '))
            result[k+2] += (((list_a[i] - 3) * ' ') + '/     \\' + ((list_a[i] - 3) * ' '))
            result[k+3] += (((list_a[i] - 4) * ' ') + '/^^^^^^^\\' +((list_a[i] - 4) * ' '))
            # head = (((i - 1) * ' ') + '/^^^\\') + '\n' + (((i - 2) * ' ') + '/     \\') + '\n'  + (((i - 3) * ' ') + '/^^^^^^^\\') + '\n'
            # # print(head)

            # สร้างตัวปราสาท
            # sand = []
            k += 4
            for j in range(k-1, list_a[i]):
                # sand.append(('/' + (((2*i) - ((2 * j) + 1)) * ' ') + '\\'))
                if j == list_a[i] - 1:
                    result[j+1] += ((((list_a[i] - j - 1) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((list_a[i] - j - 1) * ' ')))
                else:
                    result[j+1] += ((((list_a[i] - j) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((list_a[i] - j - 1) * ' ')))
            
            result[-1] += tail
        # รอบสุดท้าย
        else:
            # สร้างฐานปราสาท
            tail = ('/' + (((2 * list_a[i]) + 1) * ':' + '\\'))
            # สร้างบรรทัดว่าง
            if list_a[i] < max_height:
                for k in range(max_height - list_a[i] + 2):
                    result[k] += ' ' * (len(tail) - 1)
                    # print(result)

                
            else:
                # สร้างธง
                flag = ''
                if list_a[i] == max_height:
                    result[0] += ((list_a[i]) * ' ') + '|>>~'
                    result[1] += (((list_a[i]) * ' ') + '|')
                    k = 1

            # สร้างยอดปราสาท
            result[k+1] += (((list_a[i] - 2) * ' ') + '/^^^\\')
            result[k+2] += (((list_a[i] - 3) * ' ') + '/     \\')
            result[k+3] += (((list_a[i] - 4) * ' ') + '/^^^^^^^\\')
            # head = (((i - 1) * ' ') + '/^^^\\') + '\n' + (((i - 2) * ' ') + '/     \\') + '\n'  + (((i - 3) * ' ') + '/^^^^^^^\\') + '\n'
            # # print(head)

            # สร้างตัวปราสาท
            # sand = []
            k += 4
            for j in range(k-1, list_a[i]):
                if j == list_a[i] - 1:
                    result[j+1] += ((((list_a[i] - j - 1) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((list_a[i] - j - 2) * ' ')))
                else:
                    result[j+1] += ((((list_a[i] - j - 1) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((list_a[i] - j - 2) * ' ')))
            
            result[-1] += tail

    # result[max_height-2] = ' ' + result[max_height-2] 
    # ประกอบปราสาท
    result[-1] = result[-1].strip(' ')
    result = '\n' + '\n'.join(result)
    return result

    # print('flag:', flag)
    # print('head:', head)
    # print('sand:', sand)
    # print('tail:', tail)

    
    # result = flag + head + sand + tail
    # ['\n'.join(result) + '\n']

    # print(result)
    
    
if __name__ == '__main__':
    main()