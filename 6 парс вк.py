def parsvk(amin, amax):
    '''amin - минимальное значение id; amax - максимальное значение id
    визуальной реакции на то что код работает нет; результат только в готовом json вайле'''
    import requests
    import re
    file = open("CTF скрипт.json", "w", encoding='utf8')
    for i in range(amin, amax + 1):
        url = 'https://vk.com/id' + str(i)
        html = requests.get(url).text
        profil = (re.findall(r"op_header\">\w+\s+\w+", html))
        if set(re.findall(r"Страница удалена либо ещё не создана", html)):
            file.write(str('{'+url + ':\tСтраница удалена либо ещё не создана' + '}\n'))
            continue
        names = ''.join(profil)[11:len(''.join(profil))].split()
        if names:
            if names[1]:
                if str(names[1])[-1] == 'а':
                    sex = 'жен'
                elif (str(names[0])[-1] == 'а') or (str(names[0])[-1] == 'я') or (str(names[0])[-1] == 'a'):
                    sex = 'жен'
                else: sex = 'муж'
        if re.search(r"ClosedProfileWall PageBlock PageBlock", html):
            m = 'закрытая страница'
        elif re.search(r"Страница доступна только авторизованным пользователям", html):
            m = 'Страница доступна только авторизованным пользователям'
        else:
            m = 'открытая страница'
        file.write(str('{'+url + ':\t' + (' '.join(names)) + ',\t' + sex + ',\t' + m + '}' + '\n'))
    file.close()