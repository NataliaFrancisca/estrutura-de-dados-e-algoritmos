class Folha:
    def __init__(self, valor, esquerda, direita):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
        self.contador = 1

class ArvoreBinaria:
    def __init__(self):
        self.head = None

    def inserir(self, valor):
        if(self.head is None):
            self.head = Folha(valor, None, None)
        else:
            pai = self.head

            while(pai is not None):
                if(valor > pai.valor):
                    if(pai.direita is None):
                        pai.direita = Folha(valor, None, None)
                        break
                    if(pai.direita.valor == valor):
                        pai.direita.contador += 1
                        break
                    else:
                        pai = pai.direita

                elif(valor < pai.valor):
                    if(pai.esquerda is None):
                        pai.esquerda = Folha(valor, None, None)
                        break
                    if(pai.esquerda.valor == valor):
                        pai.esquerda.contador += 1
                        break
                    else: 
                        pai = pai.esquerda

arvorebinaria = ArvoreBinaria()

arvorebinaria.inserir(10)
arvorebinaria.inserir(8)
arvorebinaria.inserir(15)

print("ROOT: ", arvorebinaria.head.valor)
print("1. ESQUERDA: ", arvorebinaria.head.esquerda.valor)
print("1. DIREITA: ", arvorebinaria.head.direita.valor)

arvorebinaria.inserir(14)
arvorebinaria.inserir(17)
print("2. ESQUERDA: ", arvorebinaria.head.direita.esquerda.valor)
print("2. DIREITA: ", arvorebinaria.head.direita.direita.valor)

arvorebinaria.inserir(20)
arvorebinaria.inserir(2)
print("3. ESQUERDA: ", arvorebinaria.head.esquerda.esquerda.valor)
print("3. DIREITA: ", arvorebinaria.head.direita.direita.direita.valor)


arvorebinaria.inserir(1)
arvorebinaria.inserir(3)
print("4. ESQUERDA: ", arvorebinaria.head.esquerda.esquerda.esquerda.valor)
print("4. DIREITA: ", arvorebinaria.head.esquerda.esquerda.direita.valor)

arvorebinaria.inserir(4)
arvorebinaria.inserir(6)
print("5. DIREITA: ", arvorebinaria.head.esquerda.esquerda.direita.direita.valor)
print("6. DIREITA: ", arvorebinaria.head.esquerda.esquerda.direita.direita.direita.valor)

arvorebinaria.inserir(9)
arvorebinaria.inserir(0)
print("2. ESQUERDA: ", arvorebinaria.head.esquerda.direita.valor)
print("5. ESQUERDA: ", arvorebinaria.head.esquerda.esquerda.esquerda.esquerda.valor)

arvorebinaria.inserir(0)
arvorebinaria.inserir(0)
print("Contador: ", arvorebinaria.head.esquerda.esquerda.esquerda.esquerda.contador)