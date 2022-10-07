while True:
    try:
        num = int(input('Введите целое число: '))
        if num == 0:
            print('Нулевое число')
            break
        elif num > 0:
            a = 'Положительное'
        else:
            a = 'Отрицанельное'
        if num%2 == 0:
            b = 'четное'
        else:
            b = 'нечетное'
        print(a, b, 'число')
        break
    except ValueError:
        print('Введите целые числа, пожалуйста')