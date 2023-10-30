def acima_media(lista):
    over = []
    numerador = 0
    for num in lista:
        numerador += num
    media = numerador / len(lista)
    for i in lista:
        if (i > media):
            over.append(i)
    return over