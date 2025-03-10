class No:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.head = None

    def adicionarInicio(self, valor):
        if(self.head is None):
            self.head = No(valor, None)
        else:
            antigoHead = self.head
            self.head = No(valor, antigoHead)

    def adicionarFim(self, valor):
        if(self.head is None):
            self.head = No(valor, None)
        else:
            ponteiro = self.head

            while(ponteiro.proximo is not None):
                ponteiro = ponteiro.proximo
            
            ponteiro.proximo = No(valor, None)
    
    def listar(self):
        ponteiro = self.head

        while(ponteiro is not None):
            print(ponteiro.valor)
            ponteiro = ponteiro.proximo

    def buscarPorValor(self, valor):
        ponteiro = self.head

        while(ponteiro.proximo is not None):
            if(ponteiro.valor == valor):
                return ponteiro.valor
            
            ponteiro = ponteiro.proximo

        return None

    def removerInicio(self):
        novoHead = self.head.proximo
        self.head = novoHead

    def removerValor(self, valor):
        if(self.head.valor == valor):
            self.head = self.head.proximo
        else:
            ponteiro = self.head

            while(ponteiro.proximo is not None):
                ponteiroAnterior = ponteiro
                ponteiroProximo = ponteiroAnterior.proximo

                if(ponteiroProximo.valor == valor):
                    ponteiroAnterior.proximo = ponteiroProximo.proximo
                    break

                ponteiro = ponteiro.proximo

    def removerFim(self):
        ponteiro = self.head

        while(ponteiro.proximo is not None):
            ponteiroP = ponteiro.proximo

            if(ponteiroP.proximo is None):
                break

            ponteiro = ponteiro.proximo
        
        ponteiro.proximo = None


lista = Lista()

# Adicionando valores no final da lista
lista.adicionarFim(2)
lista.adicionarFim(4)
lista.adicionarFim(1)
lista.adicionarFim(3)

lista.listar()

# Removendo valor que está no começo da lista
lista.removerInicio()
print("\n")
lista.listar()

# Removendo valor que está no fim da lista
print("\n")
lista.removerFim()
lista.listar()

# Adicionando valores no inicio e no final da lista.
print("\n")
lista.adicionarInicio(23)
lista.adicionarFim(44)
lista.listar()

# Buscando pelo valor na lista
valorBusca = lista.buscarPorValor(2)
print("Resultado da busca:", valorBusca)

# Removendo valor que está em qualquer posição da lista
lista.removerValor(44)
lista.listar()
