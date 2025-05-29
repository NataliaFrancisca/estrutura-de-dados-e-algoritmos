lista = [1,3,2,1,4,2,7,1,2,3,6,12]

def maiorSublistaQueRepetoOMesmoNumeroDuasVezes(lista):
    right = 1
    left = 0
    _max = 1

    dicionario = {}
    dicionario[lista[0]] = 1

    while right < len(lista):
    
        if dicionario.get(lista[right]):
            if(dicionario[lista[right]] == 2):
                print("já existo e tem problema, pq estamos cheio...", lista[right])
                dicionario[lista[left]] -= 1
                left += 1
                print("atualizacao: ", left, right)
            else:
                print("já existo na lista, mas vou acrescentar +1.", lista[right])
                dicionario[lista[right]] += 1
                right += 1
        else:
            print("não existo na lista, mas agora vou existir.", lista[right])
            dicionario[lista[right]] = 1
            right += 1
        
        print(dicionario)
        _max = max(_max, right-left)

    print(dicionario)
    print(_max)


maiorSublistaQueRepetoOMesmoNumeroDuasVezes("aadaad");
# maiorSublistaQueRepetoOMesmoNumeroDuasVezes([1,3,2,1,4,1,7,2,3,6,12])
# maiorSublistaQueRepetoOMesmoNumeroDuasVezes([2,4,5,2,6,3,2,7,5,4,8,10,22,43,1])