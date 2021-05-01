def povtors(text):
    ''' на вход текст с повторами. если текст без повторов: выдаст пустой список '''
    t = text.split()
    return list((x, t.count(x)) for x in set(t) if t.count(x) > 1)