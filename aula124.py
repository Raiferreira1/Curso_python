# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# p1 = {
#     'nome': 'Luiz',
#     'sobrenome': 'Miranda',
# }
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
# p1.update(lista)
# print(p1)


# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        "Pergunta": "Quanto é 2+2?",
        "Opções": ["1", "3", "4", "5"],
        "Resposta": "4",
    },
    {
        "Pergunta": "Quanto é 5*5?",
        "Opções": ["25", "55", "10", "51"],
        "Resposta": "25",
    },
    {
        "Pergunta": "Quanto é 10/2?",
        "Opções": ["4", "5", "2", "1"],
        "Resposta": "5",
    },
]

acertos = 0
for perguntas in perguntas:
    print(perguntas["Pergunta"], end="\n\n")

    opçoes = perguntas["Opções"]

    for i, opção in enumerate(opçoes):
        print(f"{i}){opção}")
    print()
    
    escolha = input('Escolha uma opção:')
    escolha_int = None
    qtd_opeçoes = len(opçoes)
    acertou = False

    if escolha.isdigit():
        escolha_int = int(escolha)


    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opeçoes:
            if opçoes [escolha_int] == perguntas["Resposta"]:
               acertou = True
             
    print()
    if acertou:
        acertos += 1
        print('Voce acertou!!!')
    else:
        print('Voce erro!!!')
    print()
    
print(f'Voce acertou {acertos} perguntas de {len(perguntas)}')