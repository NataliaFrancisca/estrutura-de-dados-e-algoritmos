# Pilha (Stack)

**Pilha (ou stack)** é uma estrutura de dados do tipo `LIFO (Last In, First Out)`, ou seja, **o último elemento a entrar é o primeiro a sair.**

Imagine uma pilha de livros:
- você empilha os livros um sobre o outro.
- quando precisa pegar um livro, você tira o último que colocou.

</br>
<img src="assets/pilha-livros.png" width=600 height=200 style="display: block; margin: 0 auto"/>

## Principais Operações:
1. `push(elemento)`: adiciona um elemento ao topo da pilha
2. `pop()`: remove e retorna o elemento do topo.
3. `peek()`: retorna o elemento do tipo sem removê-lo
4. `isEmpty()`: verifica se a pilha está vazia.
5. `size()`: retorna o tamanho da pilha.

## Implementando uma Pilha:
Como a **Pilha** precisa inserir e remover elementos no topo, a **Lista Encadeada (Linked List)** pode fazer isso em `O(1)` tempo constante, pois a inserção e remoção no início/final de uma lista encadeada são operações rápidas.

### `push(valor)`: O(1) 
- sempre insere um novo elemento no topo.
- operações de **tempo constante**, pois apenas muda a referência do `head`

### `listar()`: O(n)
- precisa percorrer toda a pilha para imprimir os elementos.
- como faz um loop até o final, a complexidade é O(n)

### `peek()`: O(1)
- retorna o topo da pilha `head.titulo` sem percorrer nada.
- tempo constante.

### `pop()`: O(1)
- remove e retorna o topo da pilha
- guarda uma referência para o topo da pilha
- atualiza o topo da pilha, agora `self.head` aponta para o próximo elemento da pilha.

### `size()`: O(n)
- precisa contar os elementos da pilha percorrendo todos.
- mas é possível ser em **tempo constante**.
  
## Lógica visual de como funciona uma Pilha:

1. Ao adicionar o primeiro livro, o `head` fica como: **Canção Para Ninar Menino Grande**.
2. Ao adicionar o segundo livro, o `head` fica como: **Um defeito de Cor**;

E assim por diante, dessa forma o `head` sempre vai estar apontado para o topo da pilha. Quando usamos o método `pop` para remover o livro do topo da lista, ele muda o `head` para o próximo elemento.

</br>
<img src="assets/exemplo-logica.png" width=380 height=800 style="display: block; margin: 0 auto"/>
</br>

