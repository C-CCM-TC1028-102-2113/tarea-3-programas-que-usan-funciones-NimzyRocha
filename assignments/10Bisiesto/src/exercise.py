def tipodeaño():
    if 0 ==  año % 4:
        print ("True")
    else:
        if 0== (año % 100) or (año % 400):
            print ("False")
def main():
    #escribe tu código abajo de esta línea
    año = int(input())
    tipodeaño()
    pass

if __name__=='__main__':
    main()
