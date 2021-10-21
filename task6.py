'''
Задача 6:
Напишете скрипт , който изчислява факториел от n
(за n=5 5!= 1 * 2 * 3 * 4* 5 = 120) като n се въвежда от клавиатурата.
'''

def factoriel(n):
    # print(f'n={n}')
    if n > 1:
        return n * factoriel(n-1)
    return 1


if __name__ =='__main__':
    n = int(input(f'Enter n='))
    print(f'n!={factoriel(n)}')

