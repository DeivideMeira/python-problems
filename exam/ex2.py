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

def conceito_falta(n, f):
    perc =  f / 100
    if perc < (7 / 10):
        return "O"
    else:   
        return (conceito(n))
	