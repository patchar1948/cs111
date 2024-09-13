#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab10_1
# 204111 Sec 003

def main():
    test()


def comma_separated(n: int, group: int=3):
    result = ""
    re_n = str(n)[::-1]
    # print(re_n)
    for i in range(0,len(re_n), group):
        result = result + re_n[i: i + group] + ','
        
    if result[0] == ',':
        result = result[1:]
    if result[-1] == ',':
        result = result[:-1] 
    return result[::-1]

def test():
    assert comma_separated(3400, 3) == '3,400'
    assert comma_separated(3400, 4) == '3400'
    assert comma_separated(781588, 5) == '7,81588'
    assert comma_separated(1234) == '1,234'
    assert comma_separated(1000000) == '1,000,000'
    print("sak tee")

if __name__ == '__main__':
    main()
