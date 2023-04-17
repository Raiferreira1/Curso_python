# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def change_value(x):
    def alteration(n):
        return print(x * n)

    return alteration


duplicate = change_value(2)
triple = change_value(3)
quadruple = change_value(4)

duplicate(1)
triple(1)
quadruple(1)
