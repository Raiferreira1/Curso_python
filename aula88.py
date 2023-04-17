

"""
Tipo tupla - Uma lista imutável
"""
nomes = ['Maria', 'Helena', 'Luiz']
# nomes = tuple(nomes)

print(nomes[-1])
r,_,*_ = nomes
print(r)
print(nomes[0])