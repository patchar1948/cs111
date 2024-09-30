import string
def main():
    print(word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."))

def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    p = string.punctuation
    text = text.split()
    list_text = list(map(lambda x: x.strip(p), text))
    dict_text = dict()
    for i in list_text:
        if i in dict_text:
            dict_text[i] += 1
        else:
            dict_text[i] = 1
    return dict_text


if __name__ == '__main__':
    main()