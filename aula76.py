palavra_secreta = "xilito"
letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("informe uma letra:")
    if len(letra_digitada) > 1:
        letra_digitada = input("informe apenas uma letra:")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print("Palavra formada era:", palavra_formada)

    if palavra_formada == palavra_secreta:
        print("PARABENS VOCE ACERTOU")
        print("Total de tentativas", tentativas)
        tentativas = 0
        palavra_formada = ""
