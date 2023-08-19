# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é menor ou igual a 1
if numero <= 1:
    print("Os números menores ou iguais a 1 não são primos.")
else:
    # Assume que o número é primo inicialmente
    e_primo = True

    # Loop for para verificar se o número é divisível por algum número diferente de 1 e ele mesmo
    for i in range(2, numero):
        if numero % i == 0:
            # Se for divisível por outro número, não é primo
            e_primo = False
            break

    # Imprime o resultado
    if e_primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
