# Function to write data to a file
def write_file(file_name):
    try:
        with open(file_name, 'a') as file: # 'a' to add content to a file (without overwriting previous data)
            content = input('Digite o texto que deseja adicionar ao arquivo: ')
            file.write(content + '\n')
            print(f"Texto: '{content}' adicionado ao arquivo")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

# Function to read data from a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file: # 'r' to read
            print("\nFile contents:")
            print(file.read())
    except FileNotFoundError:
        print(f"O arquivo de nome '{file_name}' não foi encontrado")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    
# Main function
def main():
    file_name = 'dados_io.txt'

    while True:
        print("\n--- Gerenciamento de Entrada e Saída (I/O)")
        print("1. Escrever no arquivo")
        print("2. Ler do arquivo")
        print("3. Sair")

        option  = input('Selecione uma opção: ')

        if option == '1':
            write_file(file_name)
        elif option == '2':
            read_file(file_name)
        elif option == '3':
            print('Saindo do sistema...')
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    main()