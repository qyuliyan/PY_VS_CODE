#Задача 1:
#Напишете програма Конзолен Калкулатор, която пита потребителя за две
#числа и операция ( +, -, * , / , //, q-quit ) и връща резултат.
#Програмата се изпълнява до въвеждане на q.
def add_calc(a,b):
    return a+b

def substract_cals(a,b):
    return a-b

def multiply_calc(a,b):
    return a*b

def devide_calc(a,b):
    return a/b

def devide_hole_calc(a,b):
    return a//b

def quit_app(a,b):
    print('='*80)
    print('Bye!')
    quit()


if __name__ == '__main__':
    print('*'*80)
    print('Програма Конзолен Калкулатор.')
    print('пита потребителя за две числа и операция, докато не се въведе "q" за изход')
    print('*'*80)


operation=''
while operation != 'q':
    a = float(input('a = '))
    b = float(input('b = '))
    operation = input ('Изберете символ за оператор [a]dd, [s]ubstract, [m]ultiply , [d]evide , [h]ole digit devide, q-quit ')
    calculations = {
         'a':add_calc,
         's':substract_cals,
         'm':multiply_calc,
         'd':devide_calc,
         'h':devide_hole_calc,
         'q':quit_app
     }

    if operation in calculations:
        result = calculations[operation](a,b)
        print (f'result = {result}')
        print ('-'*80)

