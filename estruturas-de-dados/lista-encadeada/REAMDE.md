bn# Lista Encadeada (Linked List)

Uma Lista Encadeada (Linked List) **é uma estrutura de dados linear composta por nós (nodes)**, onde cada nó contém:
1. **dados**: o valor armazenado no nó
2. **ponteiro**: uma referência para o próximo nó
   
> Ao contrário de arrays, **as listas encadeadas não têm tamanho fixo e não exigem realocação de memória ao adicionar novos elementos.**

## Armazenamento na Memória:
As listas encadeadas **armazenam os nós dispersos pela memória, e cada nó contém um ponteiro que indica a posição nó.** Diferente de arrays, que ocupam um bloco contínuo de memória, as listas encadeadas utilizam endereços dinâmicos.

## Tipos de Listas Encadeadas:

### Lista Encadeada Simples (Singly Linked List)

- cada nó aponta para o próximo.
- percorrido apenas em um sentido.

<img src="assets/lista-simples.png"  style="display: block; margin: 0 auto"/>


### Lista Duplamente Encadeada (Doubly Linked List)
- cada nó tem um ponteiro para o próximo e para o anterior.
- pode ser percorrida em ambos os sentidos.
  
<img src="assets/lista-duplamente.png" style="display: block; margin: 0 auto"/>

### Lista Encadeada Circular (Circular Linked List)
- o último nó aponta de volta para o primeiro, formando um círculo.
  
<img src="assets/lista-circular.png" style="display: block; margin: 0 auto"/>


## Lógica visual de como funciona uma lista encadeada simples; 

Se temos uma lista encadeada que tem `head`, conseguimos adicionar elementos nela em tempo constante:

<img src="assets/lista-head.png" style="display: block; margin: 0 auto"/>
</br>

- para inserir ou remover no começo só alteramos o `head`
- **tempo constante**
  

Mas quando a lista encadeada tem `head` e `tail`, conseguimos adicionar elementos no começo e no fim da lista em tempo constante:


<img src="assets/lista-head-tail.png" style="display: block; margin: 0 auto"/>
</br>

- para inserir ou remover no fim só alteramos o `tail`
- **tempo constante**

Para fazer busca de um elemento dentro de uma lista encadeada continua sendo em tempo linear **O(n)**, porque precisamos percorrer toda a lista.

## Complexidade das Operações

A complexidade pode mudar de acordo com o tipo de lista encadeada. 


| Operação      | Complexidade |
| :---          |    :----:   |  
| Leitura      | O(n)       |
| Inserção no início   |  O(1)|
| Inserção no final   | O(n)|
| Remoção no início  |  O(1)|
| Remoção no meio  | O(n)|
| Remoção no final  |  O(n)|
