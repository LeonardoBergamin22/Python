# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Inicializa uma variável para contar as vogais
contador_vogais = 0

# Loop for para percorrer cada caractere na palavra
for letra in palavra:
    # Verifica se a letra é uma vogal (maiúscula ou minúscula)
    if letra in 'AEIOUaeiou':
        contador_vogais += 1

# Imprime o resultado
print(f"O número de vogais na palavra '{palavra}' é: {contador_vogais}")

