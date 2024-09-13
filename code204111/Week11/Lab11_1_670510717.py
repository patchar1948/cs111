    #!/usr/bin/env python3
# Patcharin Mekchang (Noon)
# 670510717
# Lab11_1
# 204111 Sec 003

def main():
    print(word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."))

def word_count(text: str) -> dict[str, int]:
    mark = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    text = text.lower()
    d = dict()
    list_text = text.split()
    # print(list_text)
    no_mark = list(map(lambda x: x.strip(mark), list_text))
    # print(no_mark)
    for i in no_mark:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1
    # print(len(d))
    return d    

if __name__ == '__main__':
    main()