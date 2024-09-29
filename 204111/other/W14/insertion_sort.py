def insertion_sort(list_a):
    size = len(list_a)
    a = list_a[:]
    for i in range(1, size):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -=1
    return a

if __name__ == '__main__':
    list_a = [6, 5, 3, 1, 8, 7, 2, 4]
    print(insertion_sort(list_a)) 