# Desenvolva um programa que contenha uma lista de livros (você deve construir com ao menos
# 5 chaves para um dicionário que representa um livro) e crie uma função para pesquisar um
# livro por título

from decimal import Decimal

def pesquisar(entrada, lista):
    return [item for item in lista if entrada.lower() in item['titulo'].lower()]

def imprimir_livros(livros):
    if len(livros) == 0:
        print('\nNenhum livro encontrado.')

    for livro in livros:
        print(f"\n--> {livro['titulo']}")
        for item, valor in livro.items():
            if item == 'titulo':
                continue
            
            if item == 'autores' and len(valor) == 1:
                print('autor:', valor[0])
                continue
            
            if type(valor) == Decimal:
                print(item + ':', f'{valor:.2f}')
                continue

            print(item + ':', valor)

livros = [
    {
        'titulo': 'O Mal-estar na Cultura',
        'autores': ['Sigmund Freud'],
        'editora': 'Internationaler Psychoanalytischer Verlag Wien',
        'ano_publicacao': 1930,
        'preco': Decimal(62.25)
    },
    {
        'titulo': 'Entendendo Algoritmos: Um Guia Ilustrado Para Programadores e Outros Curiosos',
        'autores': ['Aditya Bhargava'],
        'editora': 'Novatec Editora',
        'ano_publicacao': 2017,
        'preco': Decimal(58.50)
    },
    {
        'titulo': 'Head First Object-Oriented Analysis and Design',
        'autores': ['Brett D. McLaughlin', 'Gary Pollice', 'Dave West'],
        'editora': "O'Reilly Media",
        'ano_publicacao': 2007,
        'preco': Decimal(38.62)

    },
    {
        'titulo': "Object-Oriented Thought Process, The (Developer's Library)",
        'autores': ['Matt Weisfield'],
        'editora': "Addison-Wesley Professional",
        'ano_publicacao': 2013,
        'preco': Decimal(47.69)
    }
]

while True:
    entrada = input('\nInsira o título do livro: ')
    livros_encontrados = pesquisar(entrada, livros)

    print('\n============ Livros encontrados ============')
    imprimir_livros(livros_encontrados)

