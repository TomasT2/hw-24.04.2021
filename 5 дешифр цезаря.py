def dechifr(t):
    '''t - изначальный текст (поддерживается только английский)'''
    d = ord(t[0])-99
    s = []
    for i in range(0, len(t)):
        if (ord(t[i]) >= 97) and (ord(t[i]) <= 122):
            if (ord(str(t[i])) - d) > 122:
                s.append(chr(ord(str(t[i])) - d - 26))
                continue
            elif (ord(str(t[i])) - d) < 97:
                s.append(chr(ord(str(t[i])) - d + 26))
                continue
            s.append(chr(ord(str(t[i])) - d))
        else: s.append(t[i])
    return ''.join(s)