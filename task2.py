#Задача 2
if __name__ == '__main__':
    dict_a = {1:10, 2:20}
    dict_b = {3:30, 4:40}
    dict_c = {5:50, 6:60}
    res ={}

    res = dict_a.copy()
    res.update(dict_b)
    res.update(dict_c)
    print(res)