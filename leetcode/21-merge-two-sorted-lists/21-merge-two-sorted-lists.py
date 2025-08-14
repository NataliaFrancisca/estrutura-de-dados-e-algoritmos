def merge(listaA, listaB):
    dumb = []

    ponteiroA = 0
    ponteiroB = 0

    tamanhoListaA = len(listaA)
    tamanhoListaB = len(listaB)

    while (ponteiroA < tamanhoListaA and ponteiroB < tamanhoListaB):
        if listaA[ponteiroA] < listaB[ponteiroB]:
            dumb.append(listaA[ponteiroA])
            ponteiroA+=1
        else:
            dumb.append(listaB[ponteiroB])
            ponteiroB+=1

    valores = listaA[ponteiroA::] if ponteiroA < tamanhoListaA else listaB[ponteiroB::]
    dumb.extend(valores)
    return dumb

a = merge([1, 4, 5, 10, 21, 61, 83], [2, 3, 6, 7, 8, 32, 50]);
print(a)