def arearect (base,altura):
    area = base * altura
    return area
def main():
    #escribe tu código abajo de esta línea
    base = float (input("Dame la base: "))
    altura = float (input("Dame la altura: "))
    areat = arearect (base,altura)
    print ("El área del rectángulo es: ", float(areat))
    pass

if __name__=='__main__':
    main()
