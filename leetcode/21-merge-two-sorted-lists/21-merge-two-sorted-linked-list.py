class No:
    def __init__(self, valor=0, proximo=None):
        self.valor = valor
        self.proximo = proximo

def addNode(nodes, node):
    ponteiro = nodes

    while ponteiro.proximo is not None:
        ponteiro = ponteiro.proximo

    ponteiro.proximo = No(node, None)
    return nodes

def listar(nodes):
    ponteiro = nodes

    while ponteiro is not None:
        print(ponteiro.valor)
        ponteiro = ponteiro.proximo

def merge(listaUm, listaDois):
    dummy = No(-1)
    tail = dummy

    p1, p2 = listaUm, listaDois

    while p1 and p2:
        if p1.valor < p2.valor:
            tail.proximo = No(p1.valor, None)
            p1 = p1.proximo
        else:
            tail.proximo = No(p2.valor, None)
            p2 = p2.proximo

        tail = tail.proximo

    tail.proximo = p1 if p1 else p2
    return dummy.proximo

# Listas ligadas - simples
listaA = No(10)
listaA = addNode(listaA, 12)
listaA = addNode(listaA, 21)
listaA = addNode(listaA, 61)
listaA = addNode(listaA, 83)

listaB = No(32)
listaB = addNode(listaB, 50)

# Ligando as duas listas de forma ordenada
a = merge(listaA, listaB)
listar(a)

