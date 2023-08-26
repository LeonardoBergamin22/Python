def inverter_string():
    # Solicita que o usuário insira uma palavra
    string = input("Digite uma palavra: ")
    
    # Usando a indexação de strings para inverter a palavra
    string_invertida = string[::-1]
    
    return string_invertida

# Chamando a função e imprimindo o resultado
string_invertida = inverter_string()
print("String invertida:", string_invertida)
