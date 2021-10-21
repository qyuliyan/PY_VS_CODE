def factoriel(n):
    # print(f'n={n}')
    if n > 1:
        return n * factoriel(n-1)
    return 1


if __name__ =='__main__':
    n = int(input(f'Enter n='))
    print(f'n!={factoriel(n)}')

