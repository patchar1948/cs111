#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW04_3
# 204111 Sec 003
# TA P'Tanya

def main():

  test_is_overlapped()



def is_overlapped(l1: float, t1: float, w1: float, h1: float, l2: float, t2: float, w2: float, h2: float) -> bool:
    #l1 = int(l1); t1 = int(t1); w1 = int(w1); h1 = int(h1); l2 = int(l2); t2 = int(t2); w2 = int(w2); h2 = int(h2)
    #return(bool((0 > ((l1 + w1) - l2)) or (0 < (t1 + h1) - t2) or (0 < l1 - (l2 + w2)) or (0 > t1 - (t2 + h2)) ))
    #return(bool(l1 <= l2 <= (l1 + w1) or l1 <= (l2 + w2) <= (l1 + w1)) and (t1 <= t2 <= (t1 + h1) or t2 <= (t2 + h2) <= (t1 + h1)))

    # เปรียบเทียบค่ามากสุด - น้อยสุด ของจุดสี่เหลี่ยม ทั้งบนและล่าง (ที่ไม่ซ้อนทับกัน)
    if (max(l1, l1 + w1) < min(l2, l2 + w2)) or (min(l1, l1 + w1) > max(l2, l2 + w2)) or (max(t1, t1 + h1) < min(t2, t2 + h2)) or (min(t1, t1 + h1) > max(t2, t2 + h2)):
        return(False)
    return(True)



def test_is_overlapped():
    assert is_overlapped(10, 10, 100, 150, 50, 100, 150, 200) == True
    assert is_overlapped(10, 10, 90, 90, 150, 90, 50, 90) == False
    
    print("all ok")

if __name__ == "__main__":
  main()