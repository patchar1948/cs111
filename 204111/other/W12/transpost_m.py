def main():
    # print(transpose_matrix_1([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(transpose_matrix_3([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

def transpose_matrix_1(m):
    for i in range(0, len(m) - 1):
        if len(m[i]) != len(m[i + 1]):
            return None
    # temp = []
    result = []
    for k in range(len(m[0])):
        # print('j:', j)
        temp = []
        for j in range(len(m)):
            # count += [m[j][k]]
        # temp.append(count)
            temp.append(m[j][k])

        result.append(temp)

    return result

def transpose_matrix_2(m):
    transposed = [[row[i] for row in m] for i in range(len(m[0]))]
    return transposed

def transpose_matrix_3(m):
    print(m)
    transposed = list(zip(*m))
    print(transposed)
    # transposed = list(zip(*transposed))
    transposed = [list(row) for row in transposed]
    return transposed

if __name__ == '__main__':
    main()