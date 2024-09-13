#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW06_1
# 204111 Sec 003

def main():
    
    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))



    # test()


def decode_helper(code_table, str_index):  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
    if str_index == '.':   # ถ้าเจอ "." ให้เปลี่ยนเป็น \n เพื่อขึ้นบรรทัดใหม่
        return '\n'

    # ถ้าค่าตัวเลขที่หาตัวอักษร มากเกินกว่า จำนวน code_table หรือ ค่าตัวเลขที่หาตัวอักษร น้อยกว่า จำนวน code_table ที่ติดลบ
    if int(str_index) >= len(code_table) or int(str_index) < -len(code_table):
        return '_' # แทนค่านั้นด้วย "_"

    else:
        return code_table[int(str_index)]


def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()

    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))

    # รวม list ของอักขระ ให้เป็น string
    result = ''.join(result_list)
    return result

# def test():
#     assert (decode("aceiklmr-", '''
# 3 .
# 5 3 4 2 .
# 3 1 2 8 1 7 2 0 86 .
# -10 -1 -9 9 .
# ''')) == '''i
# like
# ice-crea_
# _-a_
# '''

#     print("@ o @")


if __name__ == '__main__':
    main()
