def str():
    try:
        counter = 0
        text = input('Text - ')
        words = text.split()
        for word in words:
            if text.count(word)>0:
                origen = text
                temp = text[0].upper() + text[1:]
                text = text.replace(origen, temp)
        print(text)
        for i in text:
            if i.isnumeric():
                counter += 1
        print(f'Num of digits - {counter}')
        res = text.count(',') + text.count('?') + text.count('!') + text.count('-') + text.count(':')
        print(f'Punctuation marks - {res}')
        res = text.count('!')
        print(f'Number of exclamation marks - {res}')
    except Exception as ex:
        print(f'Eror information: {ex}')


str()