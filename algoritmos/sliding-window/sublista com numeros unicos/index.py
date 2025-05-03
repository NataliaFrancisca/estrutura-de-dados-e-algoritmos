# tamanho máximo de uma lista com números únicos
def maiorSublistaComNumeroUnico(s):
    right = 1
    left = 0

    dicionario = {}
    dicionario[s[0]] = 1

    _max = 1

    while(right < len(s) - 1):
        right += 1  

        if(dicionario.get(s[right]) is None):
            dicionario[s[right]] = 1
        else:
            left = right
            dicionario.clear()
            dicionario[s[right]] = 1
        
        _max = max(_max, right-left+1)

    print('max', _max)

maiorSublistaComNumeroUnico([4,5,2,6,6,1,2,7,12,1,3,6,2,9,4,5,7])