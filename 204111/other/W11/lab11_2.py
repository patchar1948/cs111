def main():
    print(matching_sum((10, -1, 1, -8, 3, 1), 2))

def matching_sum(t: tuple[int], target_value: int) -> tuple[int]:
    set_result = set()
    for i in t:
        num = target_value - i
        if num in set_result:
            return [num, i]
        else:
            set_result.add(i)
    return []
if __name__ == '__main__':
    main()