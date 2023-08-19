#Abrir o arquivo no modo escrita
arquivo = open("exemplo.txt","w")

#Escrever conteudo no arquivo
arquivo.write("Ola, mundo!\n")
arquivo.write("este é um exemplo de escrita de arquivo\n")

#Fechar o arquivo
arquivo.close()
