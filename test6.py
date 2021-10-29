def process_data(*args, **kwargs):
    mcc = kwargs.get('mcc','')
    cripto_key = kwargs.get('cripto_key','')
    data = [f'{mcc}{v}' + cripto_key for v in args]
    return f'data = {data}'
 
if __name__ == '__main__':
    msisdn = 877314271
    a, b, c, d = 877989877, 453537373, 24262662, 'fgdgsdg'

    print(process_data(msisdn))
    print(process_data(a, b, c, d))
    print(process_data(a, b, c, d, mcc='+359_'))
    print(process_data(a, b, c, d, cripto_key='_1.5'))
    print(process_data(a, b, c, d, mcc='+359_', cripto_key='_2.5'))
# TODO - Dekorator to decript if cripted!!!

    # users = ['anna', 'maria', 'markus', 'jane']
    # values = [11, 12, 34, 6]
    # print(users)
    # print(*users)