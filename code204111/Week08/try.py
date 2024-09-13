def main():
    test_skip_list()


def skip_list(word: str) -> list[str]:

    skip_list_helper(word)


def skip_list_helper(word: str, start = 0, nemo = []):

    # Base Case
    if len(word) == 1:
        return list(word[0])

    # Divide & Conquer
    head = list(word[start::start + 1])
    nemo = nemo + head


    # Commbine
    return skip_list(word, start + 1, nemo)


def test_skip_list():
    print(skip_list("ABCD"))
    assert skip_list("ABCD") == ['ABCD', 'BD', 'C', 'D']
    assert skip_list("hello!") == ['hello!', 'el', 'l!', 'l', 'o', '!']
    assert skip_list("a") == ['a']
    print("Let's go to sleep")

    if __name__ == '__main__':
        main()