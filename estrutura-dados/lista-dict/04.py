# Crie um dicionário para representar uma vaga de emprego, você pode extrair as chaves
# verificando sites de ofertas de vagas. Implemente uma lista para receber algumas vagas e por
# fim desenvolva um método que ordene as vagas por valor de remuneração

from decimal import Decimal

def ordenar_por_remuneracao(vagas):
    return sorted(vagas, key=lambda vaga: vaga['salario'])    

def imprimir_vagas(vagas):
    for vaga in vagas:
        print(f"\n--> {vaga['posicao']}")
        [print(item + ':', valor) for item, valor in vaga.items() if item != 'posicao']

vagas = [
    {
        'posicao': 'Desenvolvedor Front end React Júnior',
        'remoto': True,
        'pais': 'Brasil',
        'empresa': 'Blite Tecnologia',
        'salario': Decimal(1450)
    },
    {
        'posicao': 'Remote Full-Stack JS/TS Developer',
        'remoto': True,
        'pais': 'Brasil',
        'empresa': 'Turing',
        'salario': Decimal(1900)
    },
    {
        'posicao': 'Full Stack Developer',
        'remoto': True,
        'pais': 'Estados Unidos da América',
        'empresa': 'FOURSYS',
        'salario': Decimal(2400)
    },
    {
        'posicao': 'Full-stack (Node + Next.js) Engineer',
        'remoto': False,
        'pais': 'Brasil',
        'empresa': 'Avenue Code',
        'salario': Decimal(2100)
    }
]

imprimir_vagas(ordenar_por_remuneracao(vagas))