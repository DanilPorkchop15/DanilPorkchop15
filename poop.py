while True:
    try:
        a = int(input('Введите целое число A:'))
        b = int(input('Введите целое число B:'))
        c = int(input('Введите целое число C:'))
        if a > 0 and b > 0 and c > 0:
            print('Каждое из чисел A, B, C положительное')
            break
        else:
            print('Не каждое из чисел A, B, C положительное')
    except ValueError:
        print('Введите целые числа, пожалуйста')