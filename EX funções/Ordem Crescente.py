def ordenar_em_ordem_crescente(a, b, c):
    # Coloca os três valores em uma lista e a ordena
    valores_ordenados = sorted([a, b, c])
    return valores_ordenados

# Exemplo de uso da função
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

resultado = ordenar_em_ordem_crescente(numero1, numero2, numero3)
print("Valores em ordem crescente:", resultado)
