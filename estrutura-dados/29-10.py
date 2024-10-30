# def busca_inteiro(valorBuscado, estrutura):
#     for e in range(0, len(estrutura)):
#         if valorBuscado == estrutura[e]:
#             return e
#     return -1

# lista = [1, 2, 3, 4, 5, 6]

# indice = busca_inteiro(22, lista)
# if indice >= 0:
#     print(f'Valor encontrado na posição {indice}')
# else:
#     print(f'Valor não encontrado')

import time
def bubble_sort(estrutura):
    for i in range(0, len(estrutura)):
        for j in range(0, i):
            if estrutura[i] > estrutura[j]:
                estrutura[i], estrutura[j] = estrutura[j], estrutura[i]

list = [3, 2, 1]

start = time.time()
bubble_sort(list)
end = time.time()

print(list)
print(end - start)