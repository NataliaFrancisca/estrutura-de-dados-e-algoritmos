class Livro:
    def __init__(self, titulo, proximo):
        self.titulo = titulo
        self.proximo = proximo
    
class Pilha:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1) 
    def push(self, valor):
        if(self.head is None):
            self.head = Livro(valor, None)
        else:
            proximo = self.head
            self.head = Livro(valor, proximo)

        self.size +=1

    # O(N)
    def listar(self):
        ponteiro = self.head

        while(ponteiro is not None):
            print(ponteiro.titulo)
            ponteiro = ponteiro.proximo

    # O(1)
    def peek(self):
        return self.head.titulo

    # O(1) 
    def pop(self):
        if(self.head is None):
            raise Exception("A pilha está vazia!")

        livro = self.head
        self.head = livro.proximo
        self.size -=1
        return livro.titulo
    
    def isEmpty(self):
        return self.head is None

    # O(n)
    def getSize(self):
        return self.size


pilha = Pilha()

pilha.push("Canção para ninar menino grande")
pilha.push("Um defeito de cor")
pilha.push("A cabeça do santo")
pilha.push("Se não eu, quem vai fazer você feliz?")

livroRemovido = pilha.pop()
print("Livro removido: ", livroRemovido)

livroTopo = pilha.peek()
print("Livro que está no topo: ", livroTopo)

print(pilha.isEmpty())
print(pilha.getSize())