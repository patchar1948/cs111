#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW13_1
# 204111 sec 003

def main():
    # p_list = {"chair": (0.4, 450.0), "pillow": (3.5, 315.0),
    # "stool": (0.3, 300.0), "closet": (2.5, 700.0)}
    # allowed_w = 15.0
    # budget = 1450.00
    # print(product_shopping(p_list, allowed_w, budget))
    # pass
    print(product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00))
    # assert product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00) == {'stool': 0.3,'chair': 0.4,'pillow': 3.5}

    print(product_shopping({"chair": (0.4, 450.0), "pillow": (3.5, 315.0),"stool": (0.3, 300.0), "closet": (2.5, 700.0)}, 15.0,1450.00)) #== {'stool': 0.3,'chair': 0.4,'closet': 2.5}
    print(product_shopping({"a":(0.1,10)},100.0,100.0)) #== {'a': 0.1}
    print(product_shopping({"a":(0.1,10)},100.0,1.0))# == {}
    print(product_shopping({"shirt": (0.13, 1200.), "trousers": (0.36, 850.),"jeans": (0.3, 1300.), "shoes": (0.5, 1200.),"socks": (0.15, 50.)},5.0,4200.00)) #== {'jeans': 0.3, 'shirt': 0.13, 'socks': 0.15, 'trousers': 0.36}
    print(product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96))
    #== {'w': 1, 'v': 34}

def powerset(dict_a: dict[str, tuple[float, float]]) -> list[dict[str, tuple[float, float]]]:
    # powerset
    a = [dict()]
    # want [set(), {2}, {1}, {1, 2}]
    with_2  = []
    for i in dict_a:
        # print("i:",i)
        with_2 = list(map(lambda x: x | {i: [dict_a[i][0], dict_a[i][1]]}, a))
        # print("with_2:", with_2)
        a += with_2
    print(a)
        # print("a:", a)

    return a


def check_wb(dict_a: dict[str, tuple[float, float]], weigth: int, budget: int) -> bool:
    total_w = 0
    total_b = 0
    for i in dict_a:
        total_w += dict_a[i][0]
        total_b += dict_a[i][1]
    if total_w > weigth:
        return False
    if total_b > budget:
        return False
    return True


def product_shopping(p_list: dict[str, tuple[float, float]], allowed_w: float, budget: float) -> dict[str, float]:
    # สร้างpower_dict
    power_d = powerset(p_list)
    # print(powerset(p_list))
    # print(len(power_d))
    # เลือกสินค้าที่ห้ามเกินงบ และหนักเกิน
    list_allow = list(filter(lambda x: check_wb(x, allowed_w, budget), power_d))
    if len(list_allow) == 0:
        return {}

    # เลือกสินค้าให้จำนวนชิ้นมากสุด 
    list_allow = sorted(list_allow, key=lambda x: len(x))
    maxy = len(list_allow[-1])
    # print(maxy)
    list_max = list(filter(lambda x: len(x) == maxy, list_allow))
    

    # ถ้าจำนวนชิ้นเท่ากันให้เลือกที่ น้ำหนักน้อยสุด
    if len(list_max) <= 1:
        return dict(map(lambda x: (x[0], x[1][0]) , list_max[0].items()))

    # p_list.
    list_max = sorted(list_max, key=lambda x: sum(map(lambda y: y[1][0],x.items())))
    min_w = sum(map(lambda y: y[1][0], list_max[0].items()))
    # print(min_w)

    list_min_w = list(filter(lambda x: min_w == sum(map(lambda y: y[1][0],x.items())), list_max))
    # print(list_min_w)

    # ถ้าน้ำหนักเท่ากันให้เลือกที่ ราคารวมน้อยสุด
    if len(list_min_w) <= 1:
        return dict(map(lambda x: (x[0], x[1][0]) , list_min_w[0].items()))
    
    list_min_w = sorted(list_min_w, key=lambda x: sum(map(lambda y: y[1][1],x.items())))
    # min_p = sum(map(lambda y: y[1][1], list_min_w[0].items()))
    return dict(map(lambda x: (x[0], x[1][0]) , list_min_w[0].items()))
    # print(min_w)

    # list_min_p = list(filter(lambda x: min_p == sum(map(lambda y: y[1][1],x.items())), list_min_w))
    # # print(list_min_w)

    # ถ้ายังเท่าเลือกอันไหนก็ได้


if __name__ == '__main__':
    main()