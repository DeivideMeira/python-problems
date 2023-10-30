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
        
def media_ponderada(nota1, nota2, peso1, peso2):
    if peso1 + peso2 != 0:
        return ((nota1 * peso1 + nota2 * peso2) / (peso1 + peso2))
    

def conceito_media_ponderada(nota1, nota2, peso1, peso2):
     return conceito((media_ponderada(nota1, nota2, peso1, peso2)))