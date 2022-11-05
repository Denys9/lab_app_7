def str():
    try:
        text = input('text - ')
        words = text.split()
        print(words)
        for word in words:
            if text.count(word)>0:
                origen = text
                temp = text[0].upper() + text[1:]
                text = text.replace(origen, temp)
        print(text)
        res = text.count(',') + text.count('?') + text.count('!') + text.count('!') + text.count('-') + text.count(':')
        print(f'punctuation marks - {res}')
    except Exception as ex:
        print(f'Eror information: {ex}')

str()
