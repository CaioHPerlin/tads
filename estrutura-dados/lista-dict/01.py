# Crie um Dicionário para representar um Animal. Você deve criar os atributos para reino,
# espécie, local de origem, nome científico. Desenvolva também um método para imprimir um
# animal e crie três exemplos para exemplificar

def imprimir_animal(animal):
    print(f"\n----{animal['espécie']}----")
    [print(item + ':', valor) for item,valor in animal.items()]

cachorro = {
    'reino': 'Animalia',
    'espécie': 'Cachorro',
    'local_origem': 'asia',
    'nome_cientifico': 'Canis lupus familiaris'
}

imprimir_animal(cachorro)