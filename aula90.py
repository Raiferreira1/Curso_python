lista_de_compras = []
condiçao = True
import os

while condiçao:
    op = input("Selecione um opção\n[i]nserir [a]pagar [l]ista:")

    if op == "i":
        os.system("cls")
        new_item = input("Item:")
        lista_de_compras.append(new_item)
        break

    elif op == "a":
        os.system("cls")
        indice = input("Infome o indice do item que voce quer apagar :")
        try:
            indice = int(indice)
            lista_de_compras.pop(indice)
        except TypeError:
            print("Por favor informe um valor inteiro")
        except ValueError:
            print("informe um indice existente por favor")
        except Exception:
            print("Erro desconhecido")

    elif op == "l":
        os.system("cls")
        if lista_de_compras:
            for indice, item in enumerate(lista_de_compras):
                print(indice, item)
        else:
            print("Não existem itens a serem listados")
else:
    print("Rai lindo")
