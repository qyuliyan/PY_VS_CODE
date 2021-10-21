
'''
Doc
'''
def array_processing(arr):
    sum = 0
    for i in arr:
        # print(f'{i} - {type(i)}' )
        if type(i) == int:
            sum +=i
        else:
            sum += array_processing(i)
    return sum

if __name__ =='__main__':
    arr = [1,2,[3,4],1,3,[1,[1,2,3]]]
    print(f'sum = {array_processing(arr)}')