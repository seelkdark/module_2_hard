def get_password(number):
    password = ''
    for a in range(1, number):
        for b in range(2, number):
            if b <= a:
                continue
            if number % (a + b) == 0:
                password += str(a) + str(b)
    return password
n = int(input('Введите целое число от 3 до 20: '))
result = get_password(n)
print('Пароль:', result)