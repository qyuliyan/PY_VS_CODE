'''
Задача 9
Преработете задачата за калкулата, така че за операциите да се използватламбда
изрази и да има обработка на изключения.
'''
def calc():
    actions = {
        '+': lambda a, b : a + b,
        '-': lambda a, b : a - b,
        '/': lambda a, b : a / b,
        '*': lambda a, b : a * b,
        '//' : lambda a,b: a//b

    }

    while True:
        try:
            op = input('action: + ,-, *,/, // or q-quit:')
            if op == 'q':quit()

            value1 = float(input('first number:'))
            value2 = float(input('second number:'))
            result = actions[op](value1, value2)

        except KeyError as e:
            print(f'invalid operation:{e}')
        except ValueError as e:
            print(f'invalid number:{e}')
        except ZeroDivisionError as e:
            print(f'devision by zero: {e}')
        # except Exception as e:
            # print(f'unknown error: {e}')
        else:
            print(f'{value1} {op} {value2} = {result}')
            print('--- else ---')
            continue
        finally:
            print('--- Try again ---')

if __name__ == '__main__':
    calc()   
    print('Bye!')

