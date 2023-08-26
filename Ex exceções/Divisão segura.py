def divisao_segura(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    except (TypeError, ValueError):
        return "Erro: Os parâmetros não são números válidos."

# Exemplo de uso da função
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado_divisao = divisao_segura(num1, num2)
    print("Resultado da divisão:", resultado_divisao)
except ValueError:
    print("Erro: Certifique-se de inserir números válidos.")
