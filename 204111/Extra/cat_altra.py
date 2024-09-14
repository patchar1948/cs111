#!/usr/bin/env python3
# @Author: kk
# @Last Modified time: 2022-09-24 21:16:41

cat = \
    ''' ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''


def main():
    print(cat_altar(int(input())))


def cat_altar(n):
    C_1_1 = " ／|、    "
    C_1_2 = "(°、。7   "
    C_1_3 = " |、 ~ヽ  "
    C_1_4 = " ᒐᒐ_f_ )ノ"
    C_1_5 = "__________"

    CAT_1 = [C_1_1, C_1_2, C_1_3, C_1_4, C_1_5]

    C_2_1 = " ／|、    |"
    C_2_2 = "(°、。7   |"
    C_2_3 = " |、 ~ヽ  |"
    C_2_4 = " ᒐᒐ_f_ )ノ|"
    C_2_5 = "__________|"

    CAT_2 = [C_2_1, C_2_2, C_2_3, C_2_4, C_2_5]

    C_3_1 = "| ／|、    "
    C_3_2 = "|(°、。7   "
    C_3_3 = "| |、 ~ヽ  "
    C_3_4 = "| ᒐᒐ_f_ )ノ"
    C_3_5 = "|__________"

    CAT_3 = [C_3_1, C_3_2, C_3_3, C_3_4, C_3_5]

    top = list(map(lambda x: ' ' * (((n - 1) * 11)) + x , (CAT_1)))
    # result = []

    for i in range(1, n):
        bottom = list(map(lambda x, y: (' ' * (((n-1) - i) * 11) + x) + (' ' * ((((2*i) - 1) * 11) - 1)+ y), CAT_2, CAT_3))
        top =  top + bottom

    return "\n".join(top)

if __name__ == '__main__':
    main()
