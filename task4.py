
'''
Задача 4:
Даден е масив от цели числа, който може да съдържа в себе си другимасиви (Например: [1,2,3,[5,6,[7]],4]). Напишете скрипт, който изчислява сумата на всички елементи на масива.
(За масива даден в примера:1+2+3+5+6+7+4=28)
'''
def array_processing(arr):
    sum_array = 0   # There is sum Function!!!
    for i in arr:
        # print(f'{i} - {type(i)}' )
        if type(i) is int:   # Типове се сравняват с IS!!!
            sum_array +=i
        else:
            sum_array += array_processing(i)
    return sum_array

if __name__ =='__main__':
    arr = [1,2,3,[5,6,[7]],4]
    print(f'sum_array = {array_processing(arr)}')