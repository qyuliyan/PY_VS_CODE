# 1+2+..100
def sum_numbers(n):
    print(f'n= {n}')
    if n > 0:
        return n+sum_numbers(n-1)
    return 0

if __name__ =='__main__':
    res =sum_numbers(5)
    print(res) 

    print('-'*60)