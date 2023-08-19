altura = 5  # Defina a altura do triângulo (número de linhas)
largura = altura * 2 - 1  # A largura é sempre ímpar em um triângulo equilátero

for i in range(1, altura + 1):
    espacos = " " * ((largura - (2 * i - 1)) // 2)
    asteriscos = "*" * (2 * i - 1)
    linha = espacos + asteriscos + espacos
    print(linha)
