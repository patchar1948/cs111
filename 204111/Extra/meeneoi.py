def main():
    test_meeny()
def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    # หาตำแหน่องของอักษรตัวแรกของแต่ละคำ
    a = [0] + list(map(lambda x: len(x), name_list))
    b = list(map(lambda x: len(x), name_list))
    list_index = []
    for i in range(len(a) - 2):
        list_index += [a[i + 1] + a[i]]
    list_index = [0] + list_index
    # สร้าง dict เก็บตัวแปล
    dict_name = dict()
    for i in range(len(list_index)):
        dict_name[list_index[i]] = name_list[i]
    # return (dict_name)

    # รวมชื่อเป็น list เดียว
    name_list_sum = ''.join(name_list)

    # # ทำจนกว่าจะได้ตำแน่งที่เหลือตัวเดียว
    i = 0
    count = 0
    while len(list_index) > 1:
        if i >= len(name_list_sum):
            i = 0
        if name_list_sum[i] != '*':
            count += 1

        if count == rhyme_len:
            if i in list_index: # ตำแหน่งนั้นตรงกับ list_index
                # "" + "*"* + ""
                name_list_sum = name_list_sum[:i] + ("*" * len(dict_name[i])) + (name_list_sum[i + len(dict_name[i]):])
                list_index.remove(i)
            else: 
                name_list_sum = name_list_sum[:i] + '*' + name_list_sum[i + 1:]
            # =========debug=========
            # print("=========", i, "=========")
            # print(dict_name)
            # print(name_list_sum)
            # print(i)
            # print(list_index)
            # reset count
            count = 0

        i += 1
        
    # print(dict_name[list_index[0]])
    return dict_name[list_index[0]]
            

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