import math
def str():
    try:
        text = int(input('str - '))
        list = [text]
        print(f'sum - {(list)}')
    except Exception as ex:
        print(f'Eror information: {ex}')

str()