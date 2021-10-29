'''
Стандартната функция sum() сумира списък от елемети. Напишетедекоратор
remove_duplicates, който премахва от списъка повтарящите сеелементи.
arr = [1,2,3,4,5,2,3,4]
sum(arr)
#връша 24
след прилагането на декоратора трябва да върне 15 - сумата науникалните.
Предвидете възможност за възстановяване на първоначалната sum()
'''
from functools import wraps

def remove_duplicates(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args = list(dict.fromkeys(args))
        return func(*args, **kwargs)
    return wrapper


@remove_duplicates
def sum_of_values(*args):
    result = 0
    for v in args:
        result +=v
    return result

if __name__ == '__main__':
    arr = [1,2,3,4,5,2,3,4]
    result = sum_of_values(*arr)
    print (f'result DISTINCT = {result}')
    # TODO - How to call the original function - without using the decorator?
    print (f'result ORIGINAL = {sum_of_values(*arr)}')