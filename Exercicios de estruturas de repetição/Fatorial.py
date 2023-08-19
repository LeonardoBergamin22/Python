# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa o fatorial como 1
fatorial = 1

# Verifica se o número é negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    # Calcula o fatorial usando um loop while
    while numero > 0:
        fatorial *= numero
        numero -= 1

    # Imprime o resultado
    print(f"O fatorial é: {fatorial}")
