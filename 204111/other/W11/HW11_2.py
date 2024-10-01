# def main():
    # print(split_and_merge(5))

def power_set(n: int, psl = [[]], index = 1):
    if index > n:
        return psl
    head = list(map(lambda x: x + [index], psl))
    tail = power_set(n, psl + head, index + 1)
    # print(type(tail))
    return tail

def arrive_squence(l_lane, r_lane, result = [], start_l = 0, start_r = 0):
    if len(l_lane) == start_l:
        result = result + list(r_lane[start_r:])
        return ['>'.join(result)]
    if len(r_lane) == start_r:
        result = result + list(l_lane[start_l:])
        return ['>'.join(result)]
    temp_l = result + [l_lane[start_l]]
    result_l = arrive_squence(l_lane, r_lane, temp_l, start_l + 1, start_r)

    temp_r = result + [r_lane[start_r]]
    result_r = arrive_squence(l_lane, r_lane, temp_r, start_l, start_r + 1)

    result = result_l + result_r
    return result


def split_and_merge(n: int) -> list[str]:

    ps = sorted(power_set(n), key = lambda x: len(x))
    left = ps[:len(ps) // 2]
    right = ps[len(ps) // 2:]

    result = []
    for i in range(len(left)):
        l_lane = tuple(map(lambda x: str(x), left[i]))
        r_lane = tuple(map(lambda x: str(x), right[(i * -1) -1]))
        new_result = arrive_squence(l_lane, r_lane)
        result = list(set(new_result + result))
    return result 

if __name__ == '__main__':
    print(split_and_merge(3))
