#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW11_2
# 204111 Sec 003
# TA 65-P'Ta

def main():
    print(split_and_merge(3))

def power_set(n: int, p_s_l = [[]], index_ = 1):
    if index_ > n:
        return p_s_l
    head = list(map(lambda x: x + [index_],p_s_l))
    # head = list(map(p_s_l[:]))
    tail = power_set(n, p_s_l+head, index_+1)
    
    return tail

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], result = [], st_l = 0, st_r = 0) -> list[str]:

    # Base case
    if len(l_lane) == st_l:
        result = result + list(r_lane[st_r:])
        # print([">".join(result)])
        return [">".join(result)] 

    if len(r_lane) == st_r:
        result = result + list(l_lane[st_l:])
        # print([">".join(result)])
        return [">".join(result)] 

    # D & C
    # l_lane
    temp_l = result + [l_lane[st_l]]
    result_l = arrival_sequences(l_lane, r_lane, temp_l, st_l + 1, st_r)

    # r_lane
    temp_r = result + [r_lane[st_r]]
    result_r = arrival_sequences(l_lane, r_lane, temp_r, st_l, st_r + 1)

    # Combine
    result = result_l + result_r
    return result

def split_and_merge(n: int) -> list[str]:
    ps = sorted(power_set(n), key = lambda x: len(x))
    # return(ps)
    
    def mergee(index, result):
        if index == len(ps) - 1:
            return list(set(result))
        # แบ่งเป็น 2 เลน
        l_lane = tuple(str(x) for x in ps[index]) # สร้าง lane ซ้าย
        r_lane= tuple(str(x) for x in range(1, n + 1) if x not in ps[index]) # สร้างเลนขวาที่ไม่มี ตัวด้านซ้าย

        new_result = arrival_sequences(l_lane, r_lane)
        return mergee(index + 1, result + new_result)

    return mergee(0, [])

 
if __name__ == '__main__':
    main()
    # print(split_and_merge(4))