roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# comparando os valores, sabendo que os número é um número romano válido.
def romanToInt(s):
    soma = 0
    i = 0

    while i < len(s):

        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            soma += roman[s[i + 1]] - roman[s[i]]
            i += 2
        else:
            soma += roman[s[i]]
            i += 1
        
    return soma

# comparando a letra do número romano.
def romanToInt(s):
    tamanho = len(s)
    soma = 0
    i = 0

    while i < tamanho:
        atual = s[i]

        if tamanho == i + 1:
            soma += roman[atual]
            break

        proximo = s[i + 1]

        comparacaoA = (atual == "I") and (proximo == "V" or proximo == "X")
        comparacaoB = (atual == "X") and (proximo == "L" or proximo == "C")
        comparacaoC = (atual == "C") and (proximo == "D" or proximo == "M")

        if comparacaoA or comparacaoB or comparacaoC:
            soma += roman[proximo] - roman[atual]
            i+=1
        else:
            soma += roman[atual]
        
        i+=1
            

    return soma


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
