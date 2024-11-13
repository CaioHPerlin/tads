# Implemente uma lista de contatos, para tal, você pode se basear na lista de contatos de seu
# smartphone. Adicione alguns contatos à lista e faça um método de impressão.

def imprimir_contatos(contatos):
    for cont in contatos:
        print(f"\n==== {cont['nome']} ====");
        [print(item + ':', valor) for item, valor in cont.items() if item != 'nome']

contatos = [
    {
        'nome': 'Mãe',
        'telefone': '6799780605',
        'email': 'carmenperlin@hotmail.com',
        'foto_perfil': 'https://example.com'
    },
    {
        'nome': 'Victor Hugo',
        'telefone': '6799781234',
        'email': 'victorhugoguimaraes@hotmail.com',
        'foto_perfil': 'https://example.com'
    },
    {
        'nome': 'Big C',
        'telefone': '6792198761',
        'email': '',
        'foto_perfil': 'https://example.com'
    },
    {
        'nome': 'Gustavo Ortiz',
        'telefone': '45995231234',
        'email': 'gusort@gmail.com',
        'foto_perfil': 'https://example.com'
    }
]

imprimir_contatos(contatos)