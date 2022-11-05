def str():
    try:
        text = input('str - ')
        num = input('num - ')
        print(f'count = { text.count(num)}')
    except Exception as ex:
        print(f'Eror information: {ex}')

str()