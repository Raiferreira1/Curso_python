"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
.contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segun.do dígito do CPF é 0
"""
cpf = "088.779.723-78"
cpf_Formatado = cpf.replace(".", "").replace("-", "")

soma_Total_Dos_Digitos1 = 0
contador_Regrecivo1 = 10
for digito in cpf_Formatado[:9]:
    soma_Total_Dos_Digitos1 += int(digito) * contador_Regrecivo1
    contador_Regrecivo1 -= 1

digito_Final_Um = (soma_Total_Dos_Digitos1 * 10) % 11
digito_Final_Um = digito_Final_Um if digito_Final_Um <= 9 else 0

soma_Total_Dos_Digitos2 = 0
contador_Regrecivo2 = 11
for digito in cpf_Formatado[:10]:
    soma_Total_Dos_Digitos2 += int(digito) * contador_Regrecivo2
    contador_Regrecivo2 -= 1

digito_Final_Dois = (soma_Total_Dos_Digitos2 * 10) % 11
digito_Final_Dois = digito_Final_Dois if digito_Final_Dois <= 9 else 0

dois_utimos_numeros = f"{digito_Final_Um}{digito_Final_Dois}"

if dois_utimos_numeros == cpf_Formatado[9:]:
    print("O CPF informado => " + cpf + " é valido")
else:
    print("O CPF informado => " + cpf + " não é valido")
