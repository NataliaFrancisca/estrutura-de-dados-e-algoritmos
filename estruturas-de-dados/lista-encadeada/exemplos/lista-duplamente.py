class Musica:
    def __init__(self, nome, artista):
        self.nome = nome;   
        self.artista = artista;

class Player:
    def __init__(self, anterior: Musica | None, atual: Musica, proximo: Musica | None):
        self.anterior = anterior
        self.atual = atual
        self.proximo = proximo

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def adicionar(self, musica: Musica):
        if(self.head is None):
            self.head = Player(None, musica, None)
            self.tail = None
        else:
            musicaAtual = self.head

            while(musicaAtual.proximo is not None):
                musicaAtual = musicaAtual.proximo
            
            musicaAtual.proximo = Player(musicaAtual, musica, None)
            self.tail = musicaAtual.proximo
    
    def listar(self):
        current = self.head

        while(current):
            if(current.anterior is None):
                print("anterior: ", "Nenhuma")
                print("tocando agora: ", current.atual.nome)
                print("próximo: ", current.proximo.atual.nome)
                print("\n")

            if(current.anterior is not None and current.proximo is not None):
                print("anterior: ", current.anterior.atual.nome)
                print("tocando agora: ", current.atual.nome)
                print("próximo: ", current.proximo.atual.nome)
                print("\n")

           
            if(current.proximo is None):
                print("anterior: ", current.anterior.atual.nome)
                print("tocando agora: ", current.atual.nome)
                print("próximo: ", "Nenhuma")
          
            current = current.proximo
        

playlist = Playlist()

playlist.adicionar(Musica("Caju", "Liniker"))
playlist.adicionar(Musica("Veludo Marrom", "Liniker"))
playlist.adicionar(Musica("Rio Vermelho", "Melly"))

playlist.listar()

print("Head:", playlist.head.atual.nome)
print("Tail:", playlist.tail.atual.nome)