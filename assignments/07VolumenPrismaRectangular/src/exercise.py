def area_rectangulo (base,altura):
    area = base * altura
    return area
def volumen_rectangulo (profundidad):
    areat = area_rectangulo (base,altura)
    volumen = areat * profundidad
    return volumen
def main():
    #escribe tu código abajo de esta línea
    base = float (input ("Dame la base: "))
    altura = float (input ("Dame la altura: "))
    profundidad = float (input ("Dame la profundidad: "))
    total = volumen_rectangulo (profundidad)
    print ("El volumen del prisma es: ", str(total))
    pass

if __name__=='__main__':
    main()
