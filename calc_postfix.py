def summ(a, b):
    return a+b


def sub(a, b):
    return b-a


def mul(a, b):
    return a*b


def div(a, b):
    return b/a


def calc_postfix(exp):
    """
    Выполнение операций в Postfix - “Обратная Польская Нотация”(ОПН)
    """
    stack = []
    z = 0
    funcs = {'+': summ, '-': sub, '*': mul, '/': div}
    operations = ['+', '-', '/', '*']

    for elem in exp:

        if elem in operations:

            assert elem in operations
            print('Все хорошо, операция "{}" есть в списке.'.format(elem))

            try:
                b, a = stack.pop(), stack.pop()
                print('Достать последние 2 числа из стека:', a, b)
                x = funcs[elem](b, a)
                # print('  выполнение операции funcs[elem](a, b) = ', x)
                print('  выполнение операции в Postfix ( {} {} {} ) '.format(elem, a, b))
                # if elem == '+':
                #     x = a + b
                #     # print('a + b = ', a, b, result)
                # elif elem == '-':
                #     x = a - b
                # elif elem == '*':
                #     x = a * b
                # else:
                #     x = a / b

                z = round(x, 2)
                stack.append(z)
            except ZeroDivisionError:
                print('Внимание!!! Делить на ноль нельзя!')
            except TypeError:
                print('Внимание!!! Деление на строковую переменную нельзя!')
            except UnboundLocalError:
                print('Error UnboundLocalError')
            except IndexError:
                print('Внимание!!! Введено недостаточно аргументов. ')
        else:
            try:
                x = int(elem)
                print('Считанное число = ', x)
                stack.append(x)
                print('Добавим число в стек = ', x)
            except ValueError:
                print('Внимание!!! Ошибка Значения')
    try:
        print('Результат: ', z)
    except IndexError:
        print('Error IndexError')


exp = input('Введите выражение:').split()

print(calc_postfix(exp))
