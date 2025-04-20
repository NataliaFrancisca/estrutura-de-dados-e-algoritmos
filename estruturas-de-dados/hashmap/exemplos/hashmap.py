## função hash
def simple_hash(key, size):
    return len(key) % size 

## criando uma tabela hash (hashmap)
hash_table = [
    [],
    [],
    [],
    [],
    [],
    []
]

## tamanho da tabela hash
hash_table_size = len(hash_table)

## atribuindo as variáveis o hash para cada chave (Luiz, Natalia, João)
hash_luiz = simple_hash("Luiz", hash_table_size)
hash_natalia = simple_hash("Natalia", hash_table_size)
hash_joao = simple_hash("João", hash_table_size)

## inserindo os valores na tabela hash
hash_table[hash_luiz].append(("Luiz", 120))
hash_table[hash_natalia].append(("Natalia", 200))
hash_table[hash_joao].append(("João", 100))

print(hash_table)
