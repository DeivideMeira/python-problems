def media_ponderada(w, x, y, z):
    if y + z != 0:
        return ((w * y + x * z) / (y + z))
