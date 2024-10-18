import random

print('=== Sorteador de nomes ===\n')
print(' digite fim para sortear   \n')
print('==========================')

names = []
while True:
    user_in = input('Insira um nome: ')
    if(user_in.lower() == 'fim'):
        print('==========================')
        print('Nomes:', names)
        print('Nome Sorteado:', random.choice(names))
        break
    names.append(user_in)
