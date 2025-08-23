item = input('Digite algo:')

print(type(item))
print('Só tem espaços em branco?', item.isspace())
print('É numérico?', item.isnumeric())
print('É alfabético?', item.isalpha())
print('É alfanumérico?', item.isalnum())
print('Está em maiúsculas?', item.isupper())
print('Está em minúsculas?', item.islower())
