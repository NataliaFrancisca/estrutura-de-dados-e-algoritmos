# tamanho máximo de uma lista com números únicos
def maiorSublistaComNumeroUnico(s):
    right = 1
    left = 0
    _max = 1

    if len(s) == 0:
        return 0

    dicionario = {}
    dicionario[s[0]] = 1

    while right < len(s):

        if dicionario.get(s[right]):
            dicionario[s[left]] -= 1
            left += 1
        else:
            dicionario[s[right]] = 1
            right+=1

        _max = max(_max, right-left)

    return _max
    # while(right < len(s)):
    #     if dicionario.get(s[right]):
    #         print(dicionario)
    #         dicionario[s[left]] -= 1
    #         left += 1
    #     else:
    #         dicionario[s[right]] = 1
        
    #     _max = max(_max, right-left+1)
    #     right += 1

    # print(dicionario)
    # print(left, right)
    # print('max', _max)

# maiorSublistaComNumeroUnico("dvdf")
# maiorSublistaComNumeroUnico("bbbbb")
# maiorSublistaComNumeroUnico(" ")

a = maiorSublistaComNumeroUnico("abcabcbb")
b = maiorSublistaComNumeroUnico("au")
c = maiorSublistaComNumeroUnico("")
d = maiorSublistaComNumeroUnico("   ")

print(a)
print(b)
print(c)
print(d)
# maiorSublistaComNumeroUnico([4,5,2,6,6,1,2,7,12,1,3,6,2,9,4,5,7])