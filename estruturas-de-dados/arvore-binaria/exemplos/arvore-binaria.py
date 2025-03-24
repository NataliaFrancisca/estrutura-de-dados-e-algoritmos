from collections import deque

class Folha:
    def __init__(self, valor, esquerda, direita):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
        self.contador = 1

class ArvoreBinaria:
    def __init__(self):
        self.head = None

    def exibir(self):
        if self.head is None:
            return []

        fila = deque([self.head])
        resultado = []

        while fila:
            tamanho_de_nos_por_nivel = len(fila)
            nos_do_nivel = []

            for _ in range(tamanho_de_nos_por_nivel):
                nodo = fila.popleft()
                nos_do_nivel.append(nodo.valor)

                if nodo.esquerda:

                    fila.append(nodo.esquerda)
                if nodo.direita:
  
                    fila.append(nodo.direita)

            resultado.append(nos_do_nivel)

        print(resultado)

    def inserir(self, valor):
        if(self.head is None):
            self.head = Folha(valor, None, None)
            return 
        
        pai = self.head

        while(pai is not None):
            if valor == pai.valor:
                pai.contador += 1
                return

            if valor > pai.valor:
                if pai.direita is None:
                    pai.direita = Folha(valor, None, None)
                    return
                
                pai = pai.direita
            
            elif valor < pai.valor:
                if pai.esquerda is None:
                    pai.esquerda = Folha(valor, None, None)
                    return

                pai = pai.esquerda

arvorebinaria = ArvoreBinaria()

arvorebinaria.inserir(10)
arvorebinaria.inserir(8)
arvorebinaria.inserir(15)


arvorebinaria.inserir(14)
arvorebinaria.inserir(17)

arvorebinaria.inserir(20)
arvorebinaria.inserir(2)


arvorebinaria.inserir(1)
arvorebinaria.inserir(3)


arvorebinaria.inserir(4)
arvorebinaria.inserir(6)

arvorebinaria.inserir(9)
arvorebinaria.inserir(0)

arvorebinaria.inserir(0)
arvorebinaria.inserir(0)

arvorebinaria.exibir()