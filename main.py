def str():
    try:
        text = input('text - ')
        if text.count(text) > 0:
            origen = text
            temp = text[0].upper() + text[1:]
            text = text.replace(origen, temp)
            print(text)

    except Exception as ex:
        print(f'Eror information: {ex}')

str()
