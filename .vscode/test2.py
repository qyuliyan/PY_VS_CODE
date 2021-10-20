def calc(a,b, *args):
    c= a+b

    for i in args:
        c+=i
    return c

def qqq(**qwargs):
    for q in qwargs:
        print(q)
        print(qwargs[q])

qqq(version ='1.233', port=7)


values = [i for i in range(1,4)]
print(values)
print(calc(0,0,*values))
a = '+'.join(map(str,[1,2,3]))
print(a)