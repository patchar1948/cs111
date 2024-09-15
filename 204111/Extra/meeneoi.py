# def main():
#     test_meeny()
def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    # หาตำแหน่องของอักษรตัวแรกของแต่ละคำ
    a = [0] + list(map(lambda x: len(x), name_list))
    list_index = []
    for i in range(len(a) - 2):
        list_index += [a[i + 1] + a[i]]
    list_index = [0] + list_index

    # รวมชื่อเป็น list เดียว
    name_list_sum = ''.join(name_list)

    # ทำจนกว่าจะได้ตำแน่งที่เหลือตัวเดียว
    i = 0
    count = 0
    while len(list_index) > 1:
        i += 1
        if name_list_sum[i] == '*':
            i += 1
        if count == 4:
            name_list_sum.replace(name_list_sum[i], '*')
            # reset count
            count = 0
            if i in list_index: # ตำแหน่งนั้นตรงกับ list_index
                list_index.remove(i)
        else:
            

        
        



def test_meeny():
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['John', 'Ann', 'Tom'], 5) == 'Tom'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    print("All tests passed!")

if __name__ == '__main__':
    print(eeny_meeny(['John', 'Ann', 'Tom']))
    # main()