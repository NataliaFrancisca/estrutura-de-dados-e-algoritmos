class Atendimento:
    def __init__(self, nome, proximo):
        self.nome = nome
        self.proximo = proximo

class FilaAtendimento:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0

    # O(1) 
    def isEmpty(self):
        return self.head is None

    # O(1) 
    def size(self):
        return self.tamanho

    # O(1) 
    def enqueue(self, usuario):
        atendimento = Atendimento(usuario, None)
        
        if self.isEmpty():
            self.head = atendimento
            self.tail = atendimento
        else:
            self.tail.proximo = atendimento
            self.tail = atendimento
            
        self.tamanho+=1

    # O(1) 
    def dequeue(self):
        if self.isEmpty():
            raise Exception("A fila está vazia!")
        else:
            valorRemovido = self.head
            self.head = self.head.proximo
            self.tamanho-=1

            if self.isEmpty():
                self.tail = None

            return valorRemovido.nome
    
    # O(1) 
    def peek(self):
        if(self.isEmpty()):
            raise Exception("A fila está vazia!")
        return self.head.nome
    
fila = FilaAtendimento()

fila.enqueue("Natalia")
fila.enqueue("Luiz")
fila.enqueue("Leia")

fila.dequeue()
fila.dequeue()

head = fila.peek()
print(head)
print(fila.size())