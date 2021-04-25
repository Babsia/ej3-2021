from menu import menuu
if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a ingreso por teclado")
        print("b kilos por camion")
        print("c listado de camion por dia")
        print("d salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='d'