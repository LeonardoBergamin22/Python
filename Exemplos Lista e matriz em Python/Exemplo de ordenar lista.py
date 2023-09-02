lista_original = [55,12,35,11,6]
copia =  lista_original.copy()
lista_ordenada = []

for i in range(len(lista_original)):
    elemento_minimo = min(copia)
    lista_ordenada.append(elemento_minimo)
    copia.remove(elemento_minimo)
    
    
print(lista_ordenada)
    
    
