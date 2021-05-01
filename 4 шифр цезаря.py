def chifr(t, x):
    '''t - изначальный текст (поддерживается только русский); x - смещение по алфавиту'''
    s = []
    for i in range(0,len(t)):
        if (ord(t[i]) >= 1072) and (ord(t[i]) <= 1103):
            if (ord(str(t[i])) + int(x)) > 1103:
                s.append(chr(ord(str(t[i])) + int(x) - 32))
                continue
            elif (ord(str(t[i])) + int(x)) < 1072:
                s.append(chr(ord(str(t[i])) + int(x) + 32))
                continue
            s.append(chr(ord(str(t[i])) + int(x)))
        else: s.append(t[i])
    return ''.join(s)
