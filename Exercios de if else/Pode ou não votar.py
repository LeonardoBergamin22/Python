# Solicita ao usuário que insira sua idade
idade = int(input("Digite sua idade: "))

# Verifica se a pessoa pode votar
if idade >= 16:
    print("Você pode votar nas eleições.")
else:
    print("Desculpe, você ainda não pode votar nas eleições.")
