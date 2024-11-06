prog_computadores = {
    'nome': 'Progr. de Computadores',
    'cargaHoraria': 105,
    'semestre': 2,
    'curso': 'TADS',
    'emOferecimento': True
}

estrutura_dados = {
    'nome': 'Estrutura de Dados',
    'cargaHoraria': 100,
    'semestre': 2,
    'curso': 'TADS',
    'emOferecimento': True
}

def imprimir_disciplina(obj):
    print('\n----', obj['nome'], '----')
    [print(item + ':', valor) for item,valor in obj.items()]

imprimir_disciplina(prog_computadores)
imprimir_disciplina(estrutura_dados)

estrutura_dados['ano'] = 2024
imprimir_disciplina(estrutura_dados)

estrutura_dados.pop('ano')
imprimir_disciplina(estrutura_dados)

estrutura_dados.popitem()
imprimir_disciplina(estrutura_dados)

print(estrutura_dados.keys())
print(estrutura_dados.values())
print(estrutura_dados.items())

# prog_computadores = dict(nome = 'Progr. de Computadores', cargaHoraria = 105, semestre = 2, curso = 'TADS', emOferecimento = True)
# print(prog_computadores)

