while True:
    try:
        # Solicita ao usuário que digite um número inteiro
        numero = int(input("Digite um número inteiro: "))
        
        # Calcula o quadrado do número
        quadrado = numero ** 2
        
        # Exibe o resultado
        print(f"O quadrado de {numero} é {quadrado}.")
        
        # Sai do loop
        break
    except ValueError:
        # Se ocorrer um ValueError (entrada inválida), exibe uma mensagem de erro
        print("Entrada inválida. Por favor, digite um número inteiro válido.")


