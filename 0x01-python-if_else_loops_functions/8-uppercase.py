def uppercase(str):
    for s in str:
        if 97 <= ord(s) <= 122:
            s = chr(ord(s) - 32)
        print("{}".format(s), end='')
    print("".format())
