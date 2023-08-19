#Abrir o arquivo no  modo leitura
arquivo = open("exemplo.txt","r")

#Ler conteudo do arquivo
conteudo = arquivo.read()

#Fechar o aquivo
arquivo.close()

#Imprimir o conteudo do arquivo
print(conteudo)