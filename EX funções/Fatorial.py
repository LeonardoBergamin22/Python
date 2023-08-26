def fatorial(numero):
    if numero < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Exemplo de uso da função
numero = int(input("Digite um número inteiro: "))
resultado_fatorial = fatorial(numero)

if isinstance(resultado_fatorial, int):
    print(f"O fatorial de {numero} é {resultado_fatorial}.")
else:
    print(resultado_fatorial)
