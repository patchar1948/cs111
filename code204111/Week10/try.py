
def comma_separated(n: int, group: int=3):
    result = ""
    re_n = str(n)[::-1]
    print(re_n)
    for i in range(len(str(n)) // group):
        result = str(re_n)[:group] + ',' + str(re_n)[group:]
        group = group * 2
    return result[::-1]
print(comma_separated(3400, 4))
