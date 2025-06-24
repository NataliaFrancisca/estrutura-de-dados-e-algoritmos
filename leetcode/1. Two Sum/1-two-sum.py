def two_sum(nums, target):
    dicionario = {}

    for indice, numero in enumerate(nums):
        complemento = target - numero

        if complemento in dicionario:
            return [dicionario[complemento], indice]
        
        dicionario[numero] = indice
    

a = two_sum([1, 7, 11, 15, 23, 43, 2], 9)
b = two_sum([3, 3], 6)

print(a)
print(b)