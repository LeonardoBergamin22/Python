# Função para realizar a operação de adição
def adicao(a, b):
    return a + b

# Função para realizar a operação de subtração
def subtracao(a, b):
    return a - b

# Função para realizar a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a operação de divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

# Solicita ao usuário que escolha uma operação
print("Opções:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha a operação desejada (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    resultado = adicao(num1, num2)
elif escolha == '2':
    resultado = subtracao(num1, num2)
elif escolha == '3':
    resultado = multiplicacao(num1, num2)
elif escolha == '4':
    resultado = divisao(num1, num2)
else:
    resultado = "Escolha inválida. Por favor, escolha uma opção válida."

print("Resultado: ", resultado)

        
        