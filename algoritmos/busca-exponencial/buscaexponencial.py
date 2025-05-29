lista = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,21];
listaB = [1,2,3,4,5,6]

def buscaBinaria(lista, valor, pesquerda=0, pdireita=None):
    while pesquerda <= pdireita:
        meio = (pdireita + pesquerda) // 2;

        if lista[meio] == valor:
           return meio
        
        elif lista[meio] < valor:
            pesquerda = meio + 1

        elif lista[meio] > valor:
            pdireita = meio - 1

    return -1

def buscaExponencial(lista, valor):
    if lista[0] == valor:
        return 0

    pesquerda = 0
    pdireita = 1

    while pdireita < len(lista) and lista[pdireita] < valor:
        pesquerda = pdireita
        pdireita *= 2
    
    if lista[pdireita // 2] == valor:
        return pdireita // 2

    return buscaBinaria(lista, valor, pesquerda, min(pdireita, len(lista) - 1))

a = buscaExponencial(lista, 14)
b = buscaExponencial(lista, 100)
c = buscaExponencial(listaB, 2)

print("resultado: ", a)
print("resultado: ", b)
print("resultado: ", c)