# Modele um dicionário que simbolize um carro (com as chaves: id, marca, modelo, valor,
# potência, quantidade de portas) e por fim crie um método que receba uma string como
# parâmetro, para indicar uma chave a ser removida

from decimal import Decimal

def remover_chave(chave, dict):
    dict.pop(chave)

carro = {
    'id': 1,
    'marca': 'Toyota',
    'modelo': 'Corolla 2024',
    'valor': Decimal(156000)
}


print(carro)
remover_chave('marca', carro)
print(carro)