#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab06_1
# 204111 Sec 003

def main():
    n=9                                                                 # กำหนดบรรทัดที่ใช้ในการสร้างสามเหลี่ยม = 9 
    # test_triangle()
    # n =int(input(""))/
    print(triangle(n))


def triangle(n):

    d = list(range(2 ,n)) 
    print(d)                                                            # สร้างสิสที่เป็นตรงกลาง เริ่มต้นด้วยชั้นที่ 2 จนถึงชั้นรองสุดท้าย
    c  = list(map(lambda x: '*' + ('.' *((2 * x) - 3)) + '*', d))       # สร้างแถวแต่ละแถวโดยการ แทนตัวเลขด้วย "*"

    result = '\n'.join(c)                                               # แบ่งบรรทัดด้วยการ \n
    
    # ใส่ส่วนหัวและส่วนท้าย
    result1 = ('*'+'\n') + result +'\n' + ('* ' * n ).rstrip() + '\n'   
    print(c)

    return result1


# def test_triangle():

#     T3 = '''*
# *.*
# * * *
# '''

#     T7 = '''*
# *.*
# *...*
# *.....*
# *.......*
# *.........*
# * * * * * * *
# # '''

#     assert triangle(3) == T3
#     assert triangle(7) == T7
#     print("OK")


if __name__ == '__main__':
    main()
