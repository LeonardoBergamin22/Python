# Loop for para percorrer os números de 1 a 100
for numero in range(2, 101):
    # Assume que o número é primo inicialmente
    e_primo = True

    # Verifica se o número é divisível por algum número diferente de 1 e ele mesmo
    for divisor in range(2, numero):
        if numero % divisor == 0:
            # Se for divisível por outro número, não é primo
            e_primo = False
            break

    # Se o número for primo, imprime-o
    if e_primo:
        print(numero)
