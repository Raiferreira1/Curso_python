str = 'Rai Ferreira'
i = 0
new_str = '';
while i < len(str):
    letra = str[i]
    new_str += f'*{letra}'
    i +=1

new_str += '*'
print(new_str)
