input = input().lower().strip()
input_r = input[::-1]

if input == input_r:
    print('É palíndromo')
else:
    print('Não é palíndromo')
