def SortDec3(a, b, c):
    a, b, c = max(a, b, c), a + b + c - max(a, b, c) - min(a, b, c), min(a, b, c)
    return a, b, c


while True:
    try:
        a1, b1, c1 = map(float, input('Введите через пробел три вещественных числа(a1, b1, c1): ').split())
        print(SortDec3(a1, b1, c1))
        a2, b2, c2 = map(float, input('Введите через пробел три вещественных числа(a2, b2, c2): ').split())
        print(SortDec3(a2, b2, c2))
        break
    except ValueError:
        print('Вы неправильно ввели значения, следуйте интрукциям во избежание дальнейших ошибок.\nПопробуйте заново.')
