# Willian Henrique Cardoso e Caio Hygino Perlin de Lima

imoveis = [
    {'id': 800,'tipo': 'casa', 'valor':450000, 'aluguel':False, 'cidade':'Nova Andradina', 'data_inclusao':'12/11/2014', 'metragem':80, 'contrato': 1},
    {'id': 2,'tipo': 'apartamento', 'valor':3500, 'aluguel':True, 'cidade':'Campo Grande', 'data_inclusao':'02/01/2023', 'metragem':50, 'contrato': 24},
    {'id': 3,'tipo': 'casa', 'valor':1500, 'aluguel':True, 'cidade':'Taquarussu', 'data_inclusao':'19/08/2021', 'metragem':40, 'contrato': 12},
    {'id': 4,'tipo': 'fazenda', 'valor':1450000, 'aluguel':False, 'cidade':'Nova Andradina', 'data_inclusao':'30/09/2012', 'metragem':420, 'contrato': 1},
    {'id': 5,'tipo': 'apartamento', 'valor':220000, 'aluguel':False, 'cidade':'Londrina', 'data_inclusao':'23/05/2009', 'metragem':45, 'contrato': 1},
    {'id': 6,'tipo': 'terreno', 'valor':70000, 'aluguel':False, 'cidade':'Nova Andradina', 'data_inclusao':'09/04/2019', 'metragem':90, 'contrato': 1},
    {'id': 7,'tipo': 'apartamento', 'valor':7500, 'aluguel':True, 'cidade':'Rio de janeiro', 'data_inclusao':'12/07/2024', 'metragem':110, 'contrato': 12},
]

def imprimir_imovel(imovel):
    print('Tipo:', imovel["tipo"])
    print('Metragem:', imovel["metragem"], 'm²')
    print('Data Inclusão:', imovel["data_inclusao"])
    print('Cidade:', imovel["cidade"])
    print('Disponível para ' , 'Venda' if imovel["aluguel"] == False else 'Aluguel')
    print(f'Valor: {imovel["valor"]:.2f}')
    if imovel["aluguel"] == True:
        print(f'Valor total de contrato: {(imovel["valor"]*imovel["contrato"]):.2f}')
    # se for do tipo aluguel: multiplica contrato por valor e exibe como valor total
    print('--------------------------------')

def listar_imovel_por_condicao(imoveis, aluguel):
    imoveis_filtrados = [imovel for imovel in imoveis if imovel['aluguel'] == aluguel]
    condicao_legivel = 'Venda' if not aluguel else 'Aluguel'
    if(len(imoveis_filtrados) == 0):
        return print(f'Não foram encontrados imoveis para {condicao_legivel}')

    print(f"==== < Imoveis para {condicao_legivel} > ====")
    [imprimir_imovel(imovel) for imovel in imoveis_filtrados]

def listar_imoveis_menor_que(imoveis, valor):
    imoveis_filtrados = [imovel for imovel in imoveis if imovel['valor'] < valor]
    if(len(imoveis_filtrados) == 0):
        return print(f'Não foram encontrados imoveis com valor menor que {valor}')
    
    print(f"==== < Imoveis com valor menor que {valor} > ====")
    [imprimir_imovel(imovel) for imovel in imoveis_filtrados]

def imprimir_todos_imoveis(imoveis):
    for im in imoveis:
        imprimir_imovel(im)

def corrigir_igpm(imoveis):
    igpm = int(input('Insira a porcentagem do IGP-M atual para correção (Ex: 20, 10): '))
    imoveis_aluguel = [imovel for imovel in imoveis if imovel['aluguel'] == True]

    for imovel in imoveis_aluguel:
        imovel['valor'] = imovel['valor'] * (1+igpm/100)
    
    print(f"\n{len(imoveis_aluguel)} imóveis atualizados.")
    print('--------------------------------')
    
def atualizar_imovel_por_id(imoveis):
    id = int(input('Insira o ID do imovel a ser atualizado: '))

    valor_encontrado = [im for im in imoveis if im['id'] == id]
    if(len(valor_encontrado) == 0 or valor_encontrado[0] == None): 
        print('\nImóvel não encontrado.')
        print('--------------------------------')
        return
    
    novoTipo = input('Insira o novo tipo do imóvel (Ex: casa, terreno): ')
    novoValor = int(input('Insira o novo valor do imóvel: '))
    novoAluguelInput = input('Insira se o imóvel será do tipo aluguel ou venda (a|V): ').lower()
    novoAluguel = True if novoAluguelInput == 'a' else False
    novoCidade = input('Insira a nova cidade do imóvel: ')
    novoDataDeInclusao = input('Insira a nova data de inclusão do imóvel: ')
    novoMetragem = input('Insira a nova metragem do imóvel: ')
    novoContrato = int(input('Insira o novo número de meses de contrato do imóvel (vendas apenas terão 1): '))

    imovel = valor_encontrado[0]

    imovel['tipo'] = novoTipo
    imovel['valor'] = novoValor
    imovel['aluguel'] = novoAluguel
    imovel['cidade'] = novoCidade
    imovel['data_inclusao'] = novoDataDeInclusao
    imovel['metragem'] = novoMetragem
    imovel['contrato'] = novoContrato

    print('\nImóvel atualizado.')
    print('--------------------------------')

def remover_imovel_por_id(imoveis):
    id = int(input('Insira o ID do imovel a ser removido: '))

    valor_encontrado = [im for im in imoveis if im['id'] == id]
    if(len(valor_encontrado) == 0 or valor_encontrado[0] == None): 
        print('\nImóvel não encontrado.')
        print('--------------------------------')
        return
    
    imoveis.remove(valor_encontrado[0])
    print('\nImóvel removido.')
    print('--------------------------------')

def imoveis_cidade_tipo(imoveis):
    aluguel_input = input("aluguel ou venda (a|V): ")
    aluguel = True if aluguel_input == "a" else False
    
    cidade = input("Cidade: ")
    imoveis_da_cidade = [imovel for imovel in imoveis if imovel['cidade'].lower() == cidade.lower()]

    imoveis_filtrados = [imovel for imovel in imoveis_da_cidade if imovel['aluguel'] == aluguel]
    condicao_legivel = 'Venda' if not aluguel else 'Aluguel'

    if(len(imoveis_filtrados) == 0):
        return print(f'Não foram encontrados imoveis para {condicao_legivel}')

    print(f"==== < Imoveis para {condicao_legivel} > ====")
    [imprimir_imovel(imovel) for imovel in imoveis_filtrados]

def menu(imoveis):
    opcao = 1
    while opcao != 0:
        print('=======================MENU IMÓVEIS=======================')
        print('= 1 - Listar todos imóveis                               =')
        print('= 2 - Listar imóveis do tipo Venda                        =')
        print('= 3 - Listar imóveis do tipo Aluguel                     =') #QUANDO FOR DO TIPO ALUGUEL MULTIPLICAR PELO CONTRATO + VALOR CONTRATO * valor
        print('= 4 - Lista imóveis de valor menor que                   =')
        print('= 5 - Lista imóveis da cidade com o tipo (Venda/Aluguel)  =') #USUARIO INFORMA CIDADE E TIPO DE IMOVEL
        print('= 6 - Corrigir IGP-M (REAJUSTE DE ALUGUEL)               =') #CORRIGE ALUGUEL DADO A PORCENTAGEM (ATUALIZA O VALOR APENAS DE TODOS IMOVEIS DE ALUGUEL)
        print('= 7 - Atualizar um imovel por id                         =') #ATUALIZAR SOMENTE: VALOR, ALUGUEL, DATA, METRAGEM, CONTRATO
        print('= 8 - Remover um imovel por id                           =')
        print('= 0 - Sair')
        opcao = int(input('>>'))
        if opcao == 1:
            imprimir_todos_imoveis(imoveis)
        elif opcao == 2:
            listar_imovel_por_condicao(imoveis, False)
        elif opcao == 3:
            listar_imovel_por_condicao(imoveis, True)
        elif opcao == 4:
            valor = int(input('Valor: '))
            listar_imoveis_menor_que(imoveis, valor)
        elif opcao == 5:
            imoveis_cidade_tipo(imoveis)
        elif opcao == 6:
            corrigir_igpm(imoveis)
        elif opcao == 7:
            atualizar_imovel_por_id(imoveis)
        elif opcao == 8:
            remover_imovel_por_id(imoveis)
        elif opcao == 0:
            print('Saindo!!!')
        else:
            print('Opção Inválida!')


menu(imoveis)