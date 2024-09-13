#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW10_2
# 204111 Sec 003

def main():
    test()

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


def test():
    assert sorted(arrival_sequences(('R32',), ('O9', 'O5'))) == sorted(['O9>O5>R32',
        'O9>R32>O5',
        'R32>O9>O5'])
    assert arrival_sequences(('R2', 'R4'), ('O34', 'O22')) == ['R2>R4>O34>O22',
        'R2>O34>R4>O22',
        'R2>O34>O22>R4',
        'O34>R2>R4>O22',
        'O34>R2>O22>R4',
        'O34>O22>R2>R4']
    print(arrival_sequences(('R32',), ('O9', 'O5')))
    print("Let's go to sleep")

if __name__ == "__main__":
    main()