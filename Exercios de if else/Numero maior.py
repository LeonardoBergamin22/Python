# Solicita ao usuário que insira dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual número é o maior
if numero1 > numero2:
    maior = numero1
elif numero2 > numero1:
    maior = numero2
else:
    maior = None  # Nenhum número é maior, eles são iguais

# Imprime o resultado
if maior is not None:
    print(f"O maior número é: {maior}")
else:
    print("Os números são iguais.")
