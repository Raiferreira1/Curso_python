"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

str_num = input('Informe um numero: ')

if(str_num.isdigit()):
    num = int(str_num)

    if num % 2 == 0:
        print('o numero informado é par')
    else:
        print('o numero informado é impar')
else:
    print('Voce nao digitou um numero inteiro')

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.




try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#    print('Por favor, digite apenas números inteiros')


Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

nome = input('Informe seu primeiro nome: ')
tam_name = len(nome)

if tam_name <= 4:
    print('Seu nome é curto')
elif tam_name >= 5 and tam_name <= 6:
    print('seu nome é normal')
else:
    print('Seu nome é muito grande')

"""