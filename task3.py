
def checkArrayForParticulatSym (arr , sum):
    hasParticularSum = False
    for item in arr:
        if hasParticularSum == True:
            break
        else:
            for item2 in arr:
                if item + item2 == sum:
                    print(f'{item} + {item2} = {sum}')
                    hasParticularSum = True
                    break
    if hasParticularSum == False:
        print (f'None of the couple elements in {arr} makes sum {sum} eachother')

if __name__ == '__main__':
    z = 12
    # m = [1,2,3]
    m = [1,4,6,8,9,23]
    checkArrayForParticulatSym(m,z)

    

