listaDeNomes = ["Ana", "Caio", "Bruna", "Daniel", "Eduardo", "Fernanda", "Gustavo", "Hugo", "Isabela", "João", "Kátia", "Larissa", "Maria",
"Nathalia", "Otávio", "Paula", "Quiteria", "Ricardo", "Sara", "Tatiana"]

listaDeNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def busca(lista, valor):
    ponteiroInicio = 0
    ponteiroFim = len(lista) - 1
    numeroOperacoes = 0

    while(ponteiroInicio <= ponteiroFim):
        ponteiroMeio = int((ponteiroFim + ponteiroInicio) / 2) 
        

        if(lista[ponteiroMeio] == valor):
            return "Valor encontrado: " + str(valor) + " | Número de operações: " + str(numeroOperacoes)
        if(valor < lista[ponteiroMeio]):
           ponteiroFim = ponteiroMeio - 1
        if(valor > lista[ponteiroMeio]):
            ponteiroInicio = ponteiroMeio + 1

        numeroOperacoes += 1

a = busca(listaDeNomes, "Ana")
b = busca(listaDeNomes, "João")
c = busca(listaDeNomes, "Tatiana")
d = busca(listaDeNumeros, 8)

print(a)
print(b)
print(c)
print(d)