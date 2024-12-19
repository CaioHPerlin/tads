# Alunos: Caio Hygino e Willian Cardoso

# girafa = {
#     id,
#     nome,
#     altura,
#     albina,
#     numeroDePintas,
#     sexo,
# }

girafas = []

def adicionar_girafa(lista):
    girafa = {}
    girafa['id'] = int(input('ID: '))
    girafa['nome'] = input('Nome: ')
    girafa['altura'] = float(input('Altura: '))
    girafa['albina'] = input('Albina (s/n): ').lower() == 's'
    girafa['numeroDePintas'] = int(input('Número de Pintas: '))
    girafa['sexo'] = input('sexo (m/f): ').lower()
    lista.append(girafa)
    print(girafas)

def imprimir_girafa(girafa):
    print(f"\n= Girafa N° {girafa['id']}")
    print(f"= Nome: {girafa['nome']}")
    print(f"= Sexo: {'Macho' if girafa['sexo'] == 'm' else 'Fêmea' }")
    print(f"= Altura: {girafa['altura']}m")
    print(f"= Número de Pintas: {girafa['numeroDePintas']}")
    print(f"= É Albina? {'Sim' if girafa['albina'] else 'Não' }")

# 2
def buscar_girafa_por_nome(lista, nome):
    valor_encontrado = [girafa if girafa['nome'] == nome else None for girafa in lista]
    if(len(valor_encontrado) == 0):
        return None
    return valor_encontrado


def imprimir_girafa_por_nome(lista, nome):
    girafa_encontrada = buscar_girafa_por_nome(lista, nome)
    if(girafa_encontrada == None):  
        print(f'\nNenhuma girafa com o nome {nome} encontrada')
        return

    print('> Girafa Encontrada')
    imprimir_girafa(girafa_encontrada)

# 3
def imprimir_todas_girafas(lista):
    print('==== < Girafas cadastradas > ====')
    [imprimir_girafa(girafa) for girafa in lista]

# 4 e 5
def listar_girafas_por_condicao(lista, albina):
    lista_filtrada = [girafa for girafa in lista if girafa['albina'] == albina]
    condicao_legivel = 'comuns' if not albina else 'albinas'

    if(len(lista_filtrada) == 0):
        return print(f'Não foram encontradas girafas {condicao_legivel}')

    print(f"==== < Girafas {condicao_legivel} > ====")
    [imprimir_girafa(girafa) for girafa in lista_filtrada]

# 6
def atualizar_girafa_por_nome(lista, nome):
    girafa_encontrada = buscar_girafa_por_nome(lista, nome)
    if(girafa_encontrada == None):  
        print(f'\nNenhuma girafa com o nome {nome} encontrada')

    id = girafa_encontrada['id']

    print('> Girafa Encontrada')
    imprimir_girafa(girafa_encontrada)

    print('==== < Atualização de girafa > ====')
    lista[id]['sexo'] = input("= Sexo (M/F): ")
    lista[id]['altura'] = float(input("= Altura: "))
    lista[id]['numeroDePintas'] = int(input("= Número de Pintas: "))
    inputAlbina = input("= É albina? (s/N): ")
    albina = True if inputAlbina == 'S' else False
    lista[id]['albina'] = albina
    print('Girafa atualizada com sucesso!')

# 7
def deletar_girafa(lista, nome):
    girafas_encontradas = [girafa for girafa in lista if girafa['nome'] == nome]
    
    if not girafas_encontradas:
        print(f'Nenhuma girafa com o nome {nome} encontrada')
        return
    
    for girafa in girafas_encontradas:
        lista.remove(girafa)
        print(f'Girafa {girafa["nome"]} removida com sucesso')
    
# 8
def imprimir_altura_media(lista):
    soma_alturas = sum([girafa['altura'] for girafa in lista])
    media_altura = soma_alturas / len(lista)

    print(f'\nAltura média das girafas: {media_altura:.2f}')

# 11
def numero_girafas_cadastradas():
    print(f"\nNumero de girafas cadastradas {len(girafas)}")

def menu():
    while True:
        print('\n==== < Registro de Girafas > ====')
        print('1 - Adicionar Girafa')
        print('2 - Buscar Girafa')
        print('3 - Sair')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            adicionar_girafa(girafas)
        elif opcao == '2':
            nome = input('Digite o nome da girafa: ')
            imprimir_girafa_por_nome(girafas, nome)
        elif opcao == '3':
            break
        elif opcao == '7':
            nome = input('Digite o nome da girafa: ')
            deletar_girafa(girafas, nome)
        elif opcao == '8':
            imprimir_altura_media(girafas)
        elif opcao == '11':
            numero_girafas_cadastradas()
        else:
            print('Opção inválida')

menu()