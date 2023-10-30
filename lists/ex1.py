def seleciona_pares(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares
            