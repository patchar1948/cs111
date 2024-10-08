#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Extra_12
# 204111 sec 003

('''

     |
   --*--
    /|\
   /* *\
  /* * *\
 /* * * *\
/* * * * *\
    |||
____|||____
''')

# [(' ' * (4 + n)) + ('|')]
# [(' ' * (2 + n)) + ("--*--")]
# [(' ' * (3 + n)) + ("/|\\")]
# [(' ' * (2 + n)) + ("/* *\\")]
# ((" " * (3 + n))+ ("|||"))
# (("_" * (3 + n))+ ("|||") + ("_" * (3 + n)))


def main():
    print(xmas_tree(int(input())))


def xmas_tree(n: int) -> str:
    head = ('\n' + ((' ' * (4 + n)) + ('|')) + '\n' + ((' ' * (2 + n)) + ("--*--")) + '\n' 
    + ((' ' * (3 + n)) + ("/|\\")) + '\n' + ((' ' * (2 + n)) + ("/* *\\")) + '\n')

    tail = (((" " * (3 + n))+ ("|||")) + '\n' + (("_" * (3 + n))+ ("|||") + ("_" * (3 + n))))

    t_1 = '/* * '
    t_2 = '/* * * '
    t_3 = '/* * * * '
    t_t = [t_1, t_2, t_3]
    tree = []

    for i in range(n):
        for j in range(3):
            tree += [((n + 1) - (i + j)) * " " + t_t[j] + ('* ' * i) + '*\\']
    tree = '\n'.join(tree) + '\n'
    result = head + tree + tail

    return result


if __name__ == '__main__':
    main()