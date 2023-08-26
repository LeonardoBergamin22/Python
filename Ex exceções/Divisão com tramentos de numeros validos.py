try:
    # Solicita ao usuário que insira dois números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a divisão dos números
    resultado = num1 / num2

    # Exibe o resultado da divisão
    print(f"Resultado da divisão: {resultado}")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except (ValueError, TypeError):
    print("Erro: Certifique-se de inserir números válidos.")
except Exception as e:
    print(f"Erro inesperado: {e}")
