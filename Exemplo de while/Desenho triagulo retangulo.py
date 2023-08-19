altura = int(input("Digite a altura do triângulo: "))

for i in range(altura):
    for j in range(i + 1):
        print('*', end='')
    print()
