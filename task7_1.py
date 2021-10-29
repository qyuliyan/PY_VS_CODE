'''
7.1 Напишете функция генератор, която получава като параметър цялочисло и връща
цифрите на числото.
'''
def gen(n):
    for v in n_to_string:
        yield v

if __name__ =='__main__':
    n = int(input(f'n = '))
    n_to_string = f'{n}'
    x = gen(n_to_string)
    print(next(x))
    print(next(x))
    print(next(x))
    arr = list(x)
    print(arr)