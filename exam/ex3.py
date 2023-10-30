def conceito(n):
    if n >= 9:
        return "A"
    
    elif n < 9 and n >= 8:
        return "B"

    elif n < 8 and n >= 6.5:
        return "C"

    elif n < 6.5 and n >= 5:
        return "D"

    else:
        return "F"

    
def porcentagem_aprovados(notas):
    aprovados_count = 0
    for nota in notas:
        if conceito(nota) != "F":
            aprovados_count +=1
    return (aprovados_count / len(notas) * 100)