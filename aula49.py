'''
str_num = input('Informe um numero: ')

if str_num.isdigit():
    print(f'O dobro desse numero é {2*num}')
    num = float(str_num)
else:
    print(f'{str_num} Não é um numero')
'''

str_num = input('Informe um numero: ')
try:
    print(f'Voce digitou  => {str_num}')
    num = int(str_num)
    print(f'O dobro desse numero é {2*num}')
except:
    print(f'{str_num} Não é um numero')