def firstUniqChar(s):
    dicionario = {}

    for indice, caractere in enumerate(s):
        if not dicionario.get(caractere):
            dicionario[caractere] = [indice, 1]
        else:
            dicionario[caractere][1] += 1
        
    
    for chave, valor in dicionario.items():
        if valor[1] == 1:
            return valor[0]
        
    return -1


a = firstUniqChar("natalia")
b = firstUniqChar("mariam")
c = firstUniqChar("joana")

print(a)
print(b)
print(c)