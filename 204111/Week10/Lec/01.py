# def sum_1_to_n(n):
#     result = 0

#     for i in range(n + 1):
#         result = result + i

#     return result
# print(sum_1_to_n(3))


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result = i * result
#     return result
# assert factorial(5) == 5 * 4 * 3 * 2 * 1


# def gcd(a, b):
#     r = a % b
#     while r != 0:
#         a = b
#         b = r
#         r = a % b

#     return b

# print(gcd(246, 72))


# def guess_num():
#     key = 6
#     for i in range(5):
#         n = int(input("Input number: "))
#         if n == key:
#             print(n, "is correct")
#             break
#         elif n > key:
#             print(n, "is too high")
#         else:
#             print(n, "is too low")
#     else:
#         print("guess again")
# print(guess_num())


# def score_average():
#     total_count = 3
#     score_count = 0
#     total = 0

#     while score_count < total_count:
#         score = float(input("Enter score: "))

#         if score < 0 or score > 100:
#             continue

#         total = total + score
#         score_count = score_count + 1

#     return total / score_count

# print(score_average())

# def int_power(x, y):
#     result = 1 # Initializing Condition

#     while y > 0:
#         # Modifying Condition
#         result = result * x
#         y = y - 1
#     return result

# print(int_power(2.5, 3))


# def int_to_bin(x):
#     result = ""
#     while x > 0:
#         result = str(x % 2) + result
#         x = x // 2
#     return result
# print(int_to_bin(45))


# def score_average():
#     SENTINEL = -1
#     print("Please enter students' score one for each line")
#     print("and %d for termination: " % SENTINEL)
#     total = 0.0
#     count = 0
#     while (True):
#         score = float(input(""))
#         if score == SENTINEL:
#             break
#         total += score
#         count += 1

#         if count > 0: #why do we need this?
#             average = total / count
#         else:
#             average = 0
#         print("The average of the %d numbers is %8.4f" %(count, average))

# print(score_average())


# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1
# print(find("hello", "m"))

# def count_letter(word, key):
#     count = 0

#     for letter in word:
#         if letter == key:
#             count = count + 1
#     print(count)
# count_letter("banana", "a")

# def in_both(word1, word2):
#     for letter in word1:
#         if letter in word2:
#             print(letter)
# in_both("banana", "nnn")

# def number_with_3s(lo, hi):
#     result = []
#     for x in range(lo, hi):
#         if ("3" in str(x)):
#             result.append(x)
#     return result

# print(number_with_3s(250, 304))


def merge_list(list_a, list_b):
    len_a = len(list_a)
    len_b = len(list_b)
    i = 0
    j = 0
    list_c = []

    while i < len_a and j < len_b:
        if list_a[i] < list_b[j]:
            list_c = list_c + [list_a[i]]
            i = i + 1
        else:
            list_c = list_c + [list_b[j]]
            j = j + 1

    if i < len_a:
        return list_c
    if j < len_b:
        return list_c + list_b[j:]
    return list_c


print(merge_list([1, 3, 4, 5, 6], [2, 7, 9, 10]))


def merge_list(list_a, list_b):
    if not list_a:
        return list_b
    if not list_b:
        return list_a
    if list_a[0] < list_b[0]:
        sub_task = list_a[0]
        sub_sol = merge_list(list_a[1:], list_b)
    else:
        sub_task = list_b[0]
        sub_sol = merge_list(list_a, list_b[1:])
    return [sub_task] + sub_sol


print(merge_list([1, 3, 4, 5, 6], [2, 7, 9, 10]))


# import random

# def rand_num_in_range(lo, hi):
#     return lo + (hi - lo) * random.random()

# def is_in_circle(x, y):
#     return x**2 + y**2 <= 1

# def find_pi(sample):
#     num_in_circle = 0
#     for i in range(sample):
#         x = rand_num_in_range(0, 1)
#         y = rand_num_in_range(0, 1)
#         if is_in_circle(x, y):
#             num_in_circle += 1
#     return (num_in_circle / sample) * 4

# print(find_pi(10000))
