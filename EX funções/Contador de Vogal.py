def contador_vogais():
    texto = input("Digite uma palavra ou frase: ")
    vogais = "AEIOUaeiou"
    contador = 0
    
    for char in texto:
        if char in vogais:
            contador += 1
    
    return contador

# Chamando a função e imprimindo o resultado
numero_de_vogais = contador_vogais()
print("Número de vogais na palavra ou frase:", numero_de_vogais)
