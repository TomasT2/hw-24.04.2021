def binre(text, serch):
    '''text - текст, а котором производится поиск; search - сам предме поиска
    функция выводит начало и конец совпадения в бинарном виде. если совпадений нет - пустой список'''
    import re
    f = []
    text = ' '.join(format(ord(x), 'b') for x in str(text))
    serch = ' '.join(format(ord(x), 'b') for x in str(serch))
    for match in re.finditer(serch, text):
        s = match.start()
        e = match.end()
        f.append(str(s) + '-' + str(e))
    return f

