# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def mult_int(*args):
    mult = 1
    for num in args:
        mult *= num
    return mult


variavel = mult_int(1, 2, 1, 1, 1, 2)
print(variavel)
