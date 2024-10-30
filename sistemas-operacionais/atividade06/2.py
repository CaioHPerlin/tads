# 2 - Crie uma simulação de um sistema de alocação manual de memória em Python, onde:
#     • Crie uma "memória" simulada como uma lista de tamanho fixo.
#     • Implemente funções que alocam e liberam "blocos de memória" dessa lista.

memo = [0]*10 # Lista de tamanho 10

def free_memo(index):
    if 0 > index or index >= len(memo):
        return print('Índice fora de alcance')
    
    memo.pop(index)
    print('Bloco de memória liberado.')
    print(memo)

def allocate_memo(index, val):
    if 0 > index or index >= len(memo):
        return print('Índice fora de alcance')
    
    memo[index] = val
    print('Bloco de memória alocado')
    print(memo)

print(memo)
allocate_memo(0, 1)
free_memo(0)
allocate_memo(0, 2)
allocate_memo(1, 2)
