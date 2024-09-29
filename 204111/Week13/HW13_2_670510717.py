#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW13_2
# 204111 sec 003

def main():
    print(count_vote([['Mewtwo', 'Pikachu', 'Suicune'], ['Mewtwo', 'Suicune', 'Pikachu'], ['Pikachu', 'Rayquaza', 'Charizard'], ['Suicune', 'Pikachu', 'Charizard']]))

def count_vote(pref_matrix: list[list[str]]) -> list[tuple[str, int]]:
    dict_count = dict()
    for i in range(len(pref_matrix)):
        for j in range(len(pref_matrix[i])):
            candidate = pref_matrix[i][j]
            score = (len(pref_matrix[i])) - j
            if candidate in dict_count:
                dict_count[candidate] += score
                score = 0
            else:
                dict_count[candidate] = score
                score = 0

    # print(dict_count)
    result = sorted(dict_count.items(), key = lambda x: (-x[1], x[0]), reverse = True)[::-1]
    # result = list(map(lambda x: sorted(x[0]), result0[0]))
    return result
    
    

if __name__ == '__main__':
    main()


# print(pref_matrix)
#     d_rank = dict()
#     l_p = len(pref_matrix)
#     for i in range(l_p):
#         print(i)
#         for j in range(len(pref_matrix[i])):
#             if pref_matrix[i][j] in d_rank:
#                 d_rank[i][j] += (len(pref_matrix[i]) + 1) - j
#             else:
#                 d_rank[i][j] = (len(pref_matrix[i]) + 1) - j
#     return(d_rank)