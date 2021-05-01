def rle(text):
    '''на вход текс, на выход зашифрованный'''
    lis = list(text)
    n = []
    k = 1
    for i in range(0, len(lis)):
        if i == 0: continue
        if lis[i] == lis[i - 1]:
            k = k + 1
        if lis[i] != lis[i - 1]:
            if k == 1:
                n.append(str(lis[i-1]))
            else: n.append(str(k) + str(lis[i-1]))
            k = 1
        if i==(len(lis)-1):
            if k == 1:
                n.append(str(lis[i]))
            else: n.append(str(k) + str(lis[i]))
    return ''.join(n)