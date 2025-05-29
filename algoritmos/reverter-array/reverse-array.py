arr = [1,2,3,4,5]
arr2 = [5,4,3,2,1]
arr3 = [1,2,3,4,5,6]

def reverter(arr):
    p1 = 0
    p2 = len(arr) - 1

    numero_acoes = round(len(arr) / 2)

    while numero_acoes > 0:
        valores = { p1: arr[p1], p2: arr[p2]}

        arr[p1] = valores[p2]
        arr[p2] - valores[p1]

        p1+=1
        p2-=1

        numero_acoes-=1

    print(arr)

reverter(arr)
reverter(arr2)
reverter(arr3)