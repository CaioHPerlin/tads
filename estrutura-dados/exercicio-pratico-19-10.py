# Estudante: Caio Hygino Perlin de Lima
# I
animais = ['Elefante', 'Tubarão', 'Águia', 'Leão', 'Cavalo', 'Sapo', 'Pinguim', 'Cachorro', 'Cobra', 'Gato', 'Papagaio', 'Peixe-palhaço', 'Rinoceronte', 'Girafa', 'Rã']
classificacao = ['Mamífero', 'Peixe', 'Ave', 'Mamífero', 'Mamífero', 'Anfíbio', 'Ave', 'Mamífero', 'Réptil', 'Mamífero', 'Ave', 'Peixe', 'Mamífero', 'Mamífero', 'Anfíbio']
tamanhos = [3.0, 6.0, 0.8, 1.2, 1.6, 0.1, 0.6, 0.5, 1.8, 0.4, 0.4, 0.1, 4.0, 5.5, 0.1]

def imprimir_animais_por_classe():
    # Achei que seria inteligente usar o set aqui pra extrair as classes, mas ele acaba perdendo a ordem que o sr estabeleceu no documento do exercício.
    # Portanto, deixei o set comentado, mas é uma alternativa legal pra não ter que determinar isso manualmente como na linha 10 e 20.
    # classes_ordenadas = set(classificacao)
    classes_ordenadas = ['Mamífero', 'Réptil', 'Peixe', 'Anfíbio', 'Ave']
    for classe in classes_ordenadas:
        print(f'>>>{classe}<<<')
        for i in range(len(animais)):
            if classificacao[i] == classe:
                print(f'Animal: {animais[i]}')
                print(f'Tamanho: {tamanhos[i]} metros')
        print('==========================================')

def imprimir_maiores_animais():
    classes_ordenadas = ['Mamífero', 'Peixe', 'Ave', 'Anfíbio', 'Réptil']
    for classe in classes_ordenadas:
        maior_index = tamanhos.index(max(tamanhos))
        print(f'O maior {classe.lower()} da lista é {animais[maior_index]}')
        

# O
print('===Classificação de animais vertebrados===')
imprimir_animais_por_classe()
imprimir_maiores_animais()