#!/usr/bin/env python3
# Patcharin
# 670510717
# Sec003

def main():
    test()


def  same_letters(str1: str, str2: str) -> bool:
    list_str1 = list(filter(lambda x: x.isalpha(), str1.lower()))
    #print(list_str1)
    list_str2 = list(filter(lambda x: x.isalpha(), str2.lower()))
    #print(list_str2)

    check_1 = list(map(lambda x:x in list_str2, list_str1))
    check_2 = list(map(lambda x:x in list_str1, list_str2))
    check = check_1 + check_2

    #print(check)
    # check = list(map(lambda x:True if x in list_str2 else False, list_str1))
    #print(check)
    #if check[0:] is True:
    if False in check: return False
    else: return True

def test():
    assert same_letters("your reader", "You are ready.") == True
    assert same_letters("WelCome", "weldoNe" ) is False
    assert same_letters("annA bell", "Ballean") is True 
    assert same_letters("4i2r3o{l3n}6mtG7o8d9", "GooLm#tdM4498orn23ing") is True 
    #assert same_letters("reST334RoOm344home56", "256889HBbro455om55s") is False

    same_letters("your reader", "You are ready.") 
    same_letters("WelCome", "weldoNe" )
    same_letters("annA bell", "Ballean")  
    same_letters("4i2r3o{l3n}6mtG7o8d9", "GooLm#tdM4498orn23ing")  
    same_letters("reST334RoOm344home56", "256889HBbro455om55s") 

    print("ALL OK!")

if __name__ == '__main__':
    main()
