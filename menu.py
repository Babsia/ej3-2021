from manejadorC import Manejadorcamion
from cosechas import cosecha
class menuu:
    __switcher=None
    __M=None
    __C=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.salir,
            }
        self.__M=Manejadorcamion()
        self.__M.CargarLista()
        self.__C=cosecha()
        self.__C.carga(self.__M)

        

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("opcion a")
        ids=int(input("ingrese un id de camion "))
        day=int(input("ingrese un dia "))
        self.__C.cargaporteclado(self.__M,ids,day)
        

        

    def opcion2(self):
        print("Mostrar kilos por camion")
        ids=int(input("ingrese un id de camion "))
        print("el total de kilos de el camion {} es {}".format(ids,self.__C.mostrarK(ids)))
    def opcion3(self):
        print("listado de camiones por dia")
        day=int(input("ingrese un dia "))
        self.__C.listado(self.__M,day)
