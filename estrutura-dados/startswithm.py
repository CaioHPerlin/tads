names = ['Carlos', 'João', 'Maria', 'Marcela', 'Rodrigo']
prints = [print(name) for name in names if name.lower().startswith('m')]

print(f'{len(prints)} nomes impressos.')