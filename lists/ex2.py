def seleciona_multiplos(numeros, i):
    multiplos = []
    for num in numeros:
        if num % i == 0:
            multiplos.append(num)
    return multiplos
            