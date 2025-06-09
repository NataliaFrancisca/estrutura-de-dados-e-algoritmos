class Musica:
    def __init__(self, nome):
        self.nome = nome
    
class Album:
    def __init__(self):
        self.head = None
        self.tail = None
        self.contador = 0

    def adicionar(self, musica: Musica):

        if self.head is None:
            player = Player(None, musica, None)
            self.head = player

        elif self.tail is None:
            player = Player(self.head, musica, self.head)
            self.head.proximo = player
            self.tail = player
            self.head.anterior = self.tail
            
        else:
            player = Player(self.tail, musica, self.head)

            self.tail.proximo = player
            self.head.anterior = player
            self.tail = player

        self.contador+=1

    def listar(self):
        current = self.head
        counter = 0

        while(current and counter < self.contador):
            anteriorNome = current.anterior.atual.nome if current.anterior else "Nenhuma música anterior."
            atualNome = current.atual.nome
            proximoNome = current.proximo.atual.nome if current.proximo else "Nenhuma música próximo."
        
            print(f"anterior: {anteriorNome}")
            print(f"tocando agora: {atualNome}")
            print(f"próximo: {proximoNome}")
            print("\n")

            current = current.proximo
            counter+=1
   
    
class Player:
    def __init__(self, anterior, atual: Musica, proximo):
        self.anterior = anterior
        self.atual = atual
        self.proximo = proximo


album = Album()

album.adicionar(Musica("Caju"))
album.adicionar(Musica("Veludo Marrom"))
album.adicionar(Musica("Febre"))
album.adicionar(Musica("Ajude a Salvar os Domingos"))

album.listar()
