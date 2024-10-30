import os

# Função para criar diretórios e arquivos
def criar_estrutura():
    # Definir o caminho base do projeto
    caminho_base = 'projeto_software'

    # Estrutura de diretórios
    estrutura = {
        'src': ['main.py', 'utils.py'], # Código fonte
        'docs': ['README.md', 'guia_usuario.md'], # Documentação
        'libs': [], # Bibliotecas externas
        'tests': ['test_main.py', 'test_utils.py'],
        'data': ['input_data.txt', 'output_data.txt'] # Dados de E/S
    }

    # Criar a pasta base do projeto
    if not os.path.exists(caminho_base):
        os.makedirs(caminho_base)
    
    # Criar subdiretórios e arquivos
    for diretorio, arquivos in estrutura.items():
        caminho_diretorio = os.path.join(caminho_base, diretorio)
        os.makedirs(caminho_diretorio, exist_ok=True)

        # Criar os arquivos dentrodos diretórios
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_diretorio, arquivo)
            with open(caminho_arquivo, 'w') as f:
                f.write(f'# Arquivo {arquivo}\n') # Adiciona um comentário ao arquivo
    
    print(f"Estrutura de diretórios e arquivos criada em '{caminho_base}'.")

# Executar a função para criar a estrutura
criar_estrutura()