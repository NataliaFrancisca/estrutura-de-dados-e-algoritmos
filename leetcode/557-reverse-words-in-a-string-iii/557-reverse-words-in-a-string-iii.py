def reverse(word):
    resposta = ''
    ponteiroA = 0
    ponteiroB = 0

    while(ponteiroB < len(word)):
        if(word[ponteiroB] == ' '):
            resposta += word[ponteiroA:ponteiroB][::-1]
            resposta += " "
            ponteiroA = ponteiroB + 1

        ponteiroB+=1;

    resposta += word[ponteiroA:ponteiroB][::-1]
    return resposta

print(reverse("Let's take LeetCode contest"))
print(reverse("Natalia"))
print(reverse("Natalia hoje é um bom dia."))
