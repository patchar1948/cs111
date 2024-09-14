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
C_3_5 = "|_________"

CAT_3 = [C_3_1, C_3_2, C_3_3, C_3_4, C_3_5]

def cat_altar(n):
    top = list(map(lambda x: ' ' * (((n - 1) * 10) + 1) + x , (CAT_1)))
    # result = []

    for i in range(1, n):
        bottom = list(map(lambda x, y: (' ' * (((n-1) - i) * 10) + x) + (' ' * ((((2*i) - 1) * 10))+ y), CAT_2, CAT_3))
        top =  top + bottom

    return "\n".join(top)
print(cat_altar(3))