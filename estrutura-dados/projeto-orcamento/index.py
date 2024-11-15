
key_to_readable = {
    'id': 'Código',
    'title': 'Título',
    'description': 'Descrição',
    'date': 'Data',
    'price': 'Valor',
    'active': 'Em andamento?'
}

def create_order(list, count):
    id = count

    print('======== < Cadastro de Orçamentos > ========\n')
    title = input("Insira o título do orçamento: ")
    description = input("Insira a descrição do serviço/produto oferecido: ")
    date = input("Insira a data do orçamento: ")
    price = input("Insira o valor do orçamento: ")
    active = input("Orçamento em aberto? (Y/n)").lower() != 'n'
    print('\n============================================')

    order = {
        'id': id,
        'title': title,
        'description': description,
        'date': date,
        'price': price,
        'active': active
    }

    list.append(order)


def print_all_orders(list):
    print('\n======== < Listagem de Orçamentos > ========')
    for order in list:
        print(f"\n> Orçamento {order['id']}")
        for key, value in order.items():
            print(f'{key_to_readable[key]}: {value}')
    print('\n==============================================')

def open_menu(list, counter):
    print('1 -- Criar um novo orçamento;')
    print('2 -- Ler todos os orçamentos;')
    user_option = input('Escolha uma opção:')
    
    match(user_option):
        case '1':
            create_order(list, counter)
            


orders = []
counter = 1

