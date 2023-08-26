try:
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo a ser aberto: ")

    # Tenta abrir o arquivo em modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo e o exibe
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except IOError as e:
    print(f"Erro ao abrir o arquivo: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")
