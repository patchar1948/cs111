def main():
    print(sand_towers([8, 8]))
    # print(sand_towers([7, 8, 6, 8]))

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
    for i in range(num_towers):

        # ไม่ใช่ก้อนสุดท้าย
        if i != num_towers - 1:
            # สร้างฐานปราสาท
            tail = ('/' + (((2 * list_a[i])) * ':'))

            # สร้างบรรทัดว่างไว้ด้านบน
            if list_a[i] < max_height:
                for k in range(max_height - list_a[i] + 2):
                    result[k] += '-' * (len(tail))
                    # print(result)
            else:
                # สร้างธง
                if list_a[i] == max_height:
                    result[0] += ((list_a[i]) * ' ') + '|>>~' + ((list_a[i] - 3) * ' ')
                    result[1] += (((list_a[i]) * ' ') + '|') + ((list_a[i]) * ' ')
                    k = 1

                # สร้างยอดปราสาท
            result[k+1] += (((list_a[i] - 2) * ' ') + '/^^^\\' + ((list_a[i] - 2) * ' '))
            result[k+2] += (((list_a[i] - 3) * ' ') + '/     \\' + ((list_a[i] - 3) * ' '))
            result[k+3] += (((list_a[i] - 4) * ' ') + '/^^^^^^^\\' +((list_a[i] - 4) * ' '))

            # สร้างตัวปราสาท
            k += 4
            for j in range(k, k + (list_a[i] - 4)):
                if j == k + (list_a[i] - 5):
                    # บรรทัดที่ 2 นับจากล่างขึ้นบน
                    result[j] += ((((list_a[i] - j - 1) * ' ') + '/' + (((2 * (j - 1)) - 1) * ' ') + '\\' + ((list_a[i] - j  -1) * ' ')))
                else:
                    # บรรทัดอื่นๆ (ตรงกลาง)
                    result[j] += ((((list_a[i] - j - 3) * ' ') + '/' + (((2 * (j)) + 1) * ' ') + '\\' + ((list_a[i] - (j - 1) - 1) * ' ')))
            
            result[-1] += tail
# ___________________________________________________________________________________________________________________________________________________________
        # ก้อนสุดท้าย
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


            # สร้างตัวปราสาท
            k += 4
            for j in range(k-1, list_a[i]):
                if j == list_a[i] - 1:
                    result[j+1] += ((((list_a[i] - j - 1) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((list_a[i] - j - 2) * ' ')))
                else:
                    result[j+1] += ((((list_a[i] - j - 1) * ' ') + '/' + (((2 * j) + 1) * ' ') + '\\' + ((list_a[i] - j - 2) * ' ')))
            
            result[-1] += tail
    
    result[-1] = result[-1].strip(' ')
    result = '\n' + '\n'.join(result)
    return result

if __name__ == '__main__':
    main()

    

    

