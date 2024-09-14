#!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# HW08_2
# 204111 Sec 003

def main():

    test_is_anagram()

def is_anagram(s1: str, s2: str) -> bool:

    if s1 == '' and s2 == '':
        return True

    s1 = list(s1.lower().replace(' ', ''))
    # print(s1)
    s2 = list(s2.lower().replace(' ', ''))
    # print(s2)

    new_s1 = ''.join(list(filter(lambda x:x.isalpha(), s1)))
    new_s2 = ''.join(list(filter(lambda x:x.isalpha(), s2)))

    if len(new_s1) < len(new_s2) or len(new_s1) > len(new_s2):
        return False


    shark = new_s2.find(new_s1[0])

    if shark == -1:
        return False

    else:
        new_s2 = new_s2.replace(new_s1[0], '', 1)
        new_s1 = new_s1.replace(new_s1[0], '', 1)
        return is_anagram(new_s1, new_s2)


def test_is_anagram():
    assert is_anagram("Tom Marvolo Riddle", "I am Lord Voldemort!!!") is True
    assert is_anagram("cat", "tab") is False
    assert is_anagram("!!!", "tab") is False
    assert is_anagram("Nissan", "Insane") is False
    print("Let's go to sleep")

if __name__ == '__main__':
    main()