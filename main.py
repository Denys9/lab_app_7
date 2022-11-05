import statistics
def str():
   try:
        list = []
        print('To break ')
        text = 0
        while True:
                text = int(input('text->'))
                if text > 0:
                    list.append(text)
                else:
                    break


        summary = sum(list)
        length = len(list)
        avg = summary / length
        print(avg)
   except Exception as ex:
        print(f'Error: {ex}')
str()
