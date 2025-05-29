lista = [2,3,4,5,6,7,8,9,14,15,16,19,21];
listaB = [1,2,3,4,5,6]

def buscaBinaria(lista, valor, pesquerda, pdireita):
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

    pdireita = 1

    while pdireita < len(lista):
       pdireita *= 2

    return buscaBinaria(lista, valor, 0, pdireita)

a = buscaExponencial(lista, 14)
b = buscaExponencial(lista, 10)
c = buscaExponencial(listaB, 2)

print(a)
print(b)
print(c)