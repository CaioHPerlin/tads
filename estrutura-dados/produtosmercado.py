
# Lista de produtos e preços mercado A
produtos_mercado_a = ['Arroz', 'Feijão', 'Macarrão', 'Leite', 'Açúcar', 'Café', 'Óleo', 'Pão', 'Carne', 'Queijo']
precos_mercado_a = [5.99, 7.5, 5.4, 4.49, 2.79, 9.99, 6.25, 1.89, 25.00, 18.9]

# Lista de produtos e preços mercado B
produtos_mercado_b = ['Chá', 'Queijo', 'Feijão', 'Macarrão', 'Farinha', 'Açúcar', 'Café', 'Azeite', 'Refrigerante', 'Carne', 'Shampoo', 'Detergente']
precos_mercado_b = [3.99, 27.8, 9.5, 3.2, 8.0, 2.79, 9.99, 26.25, 8.89, 27.0, 18.90, 3.5]

def calc_menor_preco_produto(produto):

    index_mercado_a = produtos_mercado_a.index(produto) if produto in produtos_mercado_a else None
    index_mercado_b = produtos_mercado_b.index(produto) if produto in produtos_mercado_b else None

    if index_mercado_a == None:
        return ['B', precos_mercado_b[index_mercado_b]]
    
    if index_mercado_b == None:
        return ['A', precos_mercado_a[index_mercado_a]]
    
    preco_a = precos_mercado_a[index_mercado_a]
    preco_b = precos_mercado_b[index_mercado_b]

    return ['A', preco_a] if preco_b > preco_a else ['B', preco_b]

produtos = set(produtos_mercado_a + produtos_mercado_b)

for produto in produtos:
    resultado = calc_menor_preco_produto(produto)
    mercado = resultado[0]
    preco = resultado[1]
    print(f'{produto}: mais barato no Mercado {mercado}, custando R${preco:.2f}')
