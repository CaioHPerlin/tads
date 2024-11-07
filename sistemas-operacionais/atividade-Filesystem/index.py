import os
import shutil

def criar_pasta(caminho):
    try:
        os.makedirs(caminho)
        print(f"Pasta '{caminho}' criada com sucesso.")
    except FileExistsError:
        print(f"A pasta '{caminho}' já existe.")

def renomear(caminho, novo_nome):
    try:
        os.rename(caminho, novo_nome)
        print(f"'{caminho}' renomeado para '{novo_nome}'.")
    except FileNotFoundError:
        print(f"O caminho '{caminho}' não existe.")

def deletar(caminho):
    if os.path.isdir(caminho):
        shutil.rmtree(caminho)
        print(f"Pasta '{caminho}' deletada.")
    elif os.path.isfile(caminho):
        os.remove(caminho)
        print(f"Arquivo '{caminho}' deletado.")
    else:
        print(f"O caminho '{caminho}' não existe.")

def listar_conteudo(caminho):
    try:
        conteudo = os.listdir(caminho)
        print(f"Conteúdo de '{caminho}':")
        for item in conteudo:
            print(item)
    except FileNotFoundError:
        print(f"O caminho '{caminho}' não existe.")

def criar_arquivo(caminho):
    try:
        with open(caminho, 'w') as arquivo:
            arquivo.write("Conteúdo inicial do arquivo")
        print(f"Arquivo '{caminho}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar arquivo '{caminho}': {e}")

def mover_arquivo(origem, destino):
    try:
        shutil.move(origem, destino)
        print(f"Arquivo movido de '{origem}' para '{destino}'.")
    except FileNotFoundError:
        print(f"O arquivo '{origem}' não existe.")

def copiar_arquivo(origem, destino):
    try:
        shutil.copy2(origem, destino)
        print(f"Arquivo copiado de '{origem}' para '{destino}'")
    except FileNotFoundError:
        print(f"O arquivo '{origem}' não existe.")

def menu():
    print("\nSistema de Arquivos Básico")
    print("1. Criar pasta")
    print("2. Renomear arquivo/pasta")
    print("3. Deletar arquivo/pasta")
    print("4. Listar conteúdo da pasta")
    print("5. Criar arquivo")
    print("6. Mover arquivo")
    print("7. Copiar arquivo")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

if __name__ == "__main__":
    while True:
        opcao = menu()

        if opcao == '1':
            caminho = input("Digite o caminho da nova pasta: ")
            criar_pasta(caminho)
        elif opcao == '2':
            caminho = input("Digite o caminho atual: ")
            novo_nome = input("Digite o novo nome: ")
            renomear(caminho, novo_nome)
        elif opcao == '3':
            caminho = input("Digite o camiho do arquivo/pasta para deletar: ")
            deletar(caminho)
        elif opcao == '4':
            caminho = input("Digite o caminho da pasta: ")
            listar_conteudo(caminho)
        elif opcao == '5':
            caminho = input("Digite o caminho do novo arquivo: ")
            criar_arquivo(caminho)
        elif opcao == '6':
            origem = input("Digite o caminho do arquivo de origem: ")
            destino = input("Digite o destino: ")
            mover_arquivo(origem, destino)
        elif opcao == '7':
            origem = input("Digite o caminho do arquivo de origem: ")
            destino = input("Digite o destino: ")
            copiar_arquivo(origem, destino)
        if opcao == '0':
            print("Saindo do sistema de arquivo.")
            break
        else:
            print("Opção inválida, tente novamente.")