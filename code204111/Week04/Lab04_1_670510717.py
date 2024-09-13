#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab04_1
# 204111 Sec 003

from math import isclose

def main():
    test_circle_intersect()



def circle_intersect(x1: float, y1: float, r1: float, x2: float, 
                    y2: float, r2: float, epsilon=10**-6) -> int:
    
    distance = ((((x1 - x2)**2) + ((y1 - y2)**2)) ** 0.5) # ระยะห่างระหว่างจุดศูนย์กลางของวงกลม 2 วง
    circle_distance = distance - (r1 + r2) # ระยะห่างระหว่างเส้นรอบวงของวงกลม 2 วง
    #circle_distance = abs(circle_distance)
    #print(circle_distance)
    

    # วงกลมซ้อนทับกัน
    if (isclose(circle_distance, 0, abs_tol = epsilon)):
        return 0


    # เส้นรอบวงสัมผัสกันพอดี
    if circle_distance < 0:
        return 1 

   
    # วงกลมไม่ซ้อนทับกัน
    if circle_distance > 0:
        return -1



def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    #  now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon = 1.5) == 0
    print("all ok!")


if __name__ == '__main__':
    main()