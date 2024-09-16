def main():
    test_meeny()
def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    # Ex. ['John', 'Ann', 'Tom']
    first = list(map(lambda x: x[0], name_list)) # first = ['J', 'A', 'T']
    first_index = list(map(lambda x: len(x), name_list)) # first_index = [4, 3, 3]
    dict_name = dict(map(lambda x: (sum(first_index[:x]), name_list[x]), range(len(first_index)))) # dict_name = {0: 'John', 4: 'Ann', 7: 'Tom'}
    # print(dict_name)

    # รวมชื่อเป็น list เดียว
    name_list_sum = list(''.join(name_list)) # name_list_sum = ['J', 'o', 'h', 'n', 'A', 'n', 'n', 'T', 'o', 'm']
    # print(name_list_sum)

    # ================================================================= #
    i = 0
    count = 0
    while len(name_list) > 1: # ทำก็ต่อเมื่อ len(name_list) > 1
        i = i % len(name_list_sum) # คิดค่า i ว่าต้อง run กีรอบ

        if name_list_sum[i] == '*': # ถ้าเจอ '*' เลื่อน i ไป 1 ตำแหน่ง
            i += 1

        elif count == rhyme_len - 1: # ถ้า count = (rhyhme_len - 1) ที่ - 1 เพราะว่า count เริ่มที่ 1
            if name_list_sum[i] in first: # ถ้า name_list_sum ตำแหน่งนั้น อยู่ใน first Ex. ['J', 'A', 'T']
                # "" + "*"* + ""
                name_list.remove(dict_name[i]) # remove name_list Ex. ['John', 'Ann', 'Tom'] ---> ['John', 'Ann']
                # print(name_list)
                name_list_sum = name_list_sum[:i] + (["*"] * len(dict_name[i])) + (name_list_sum[i + len(dict_name[i]):])
                #  ['J', 'o', 'h', '*', 'A', 'n', 'n', 'T', 'o', 'm'] ---> ['J', 'o', 'h', '*', 'A', 'n', 'n', '*', '*', '*'] ( ลงที่ตัว 'T')
                # print(name_list_sum)

                if len(name_list_sum) == 1:
                    return name_list[0]

            else: # ตัวอื่นที่ไม่ใช้ตัวที่อยู่ใน first
                name_list_sum[i] = "*"
            i += 1
            count = 0
        else:
            i += 1
            count += 1

            # =========debug=========
            # print("=========", i, "=========")
            # print(dict_name)
            # print(name_list_sum)
            # print(i)
            # print(name_list)
        
    return name_list[0]
            

def test_meeny():
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['John', 'Ann', 'Tom'], 5) == 'Tom'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    print("All tests passed!")

if __name__ == '__main__':
    # print(eeny_meeny(['John', 'Ann', 'Tom']))
    main()