listaDeNomes = ["Ana", "Caio", "Bruna", "Daniel", "Eduardo", "Fernanda", "Gustavo", "Hugo", "Isabela", "João", "Kátia", "Larissa", "Maria",
"Nathalia", "Otávio", "Paula", "Quiteria", "Ricardo", "Sara", "Tatiana"]

listaDeNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def busca(lista, valor):
    numeroOperacoes = 0

    for i in range(len(lista)):
        numeroOperacoes += 1

        if(lista[i] == valor):
            return "Valor encontrado: " + str(valor) + " | Número de operações: " + str(numeroOperacoes)
        
        
a = busca(listaDeNomes, "Ana")
b = busca(listaDeNomes, "João")
c = busca(listaDeNumeros, 8)

print(a)
print(b)
print(c)