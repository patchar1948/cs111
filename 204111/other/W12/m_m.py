def main():
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 9, 10]], [[1, 2, 3], [4, 5, 6], [7, 9, -1]]))
def sum_matrix(m1, m2):
    if len(m1) != len(m2):
        return None

    for row in range(len(m1)):
        if len(m1[row]) != len(m2[row]):
            return None

    result = []
    for i in range(len(m1)):
        temp = []
        for j in range(len(m1[i])):
            temp += [m1[i][j] +  m2[i][j]]
            # temp.append(m1[i][j] + m2[i][j])
        result += [temp]
    return result

if __name__ == '__main__':
    main()
        

