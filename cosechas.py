
from manejadorC import Manejadorcamion
import csv
class cosecha:
    __lista=[]
    def __init__(self):
        for i in range (20):
            self.__lista.append([])
            for j in range (45):
                self.__lista[i].append(0)
    def carga(self,lcamion):
        archi=open('cosechas.csv')
        reader=csv.reader(archi,delimiter=',')
        for fila in reader:
            i=int(fila[0])-1
            j=int(fila[1])-1
            total=int(fila[2])-int(lcamion.tara(i))
            self.__lista[i][j]=int(total)
    def cargaporteclado(self,lcamion,ids,dia):
        dia=dia-1
        ids=ids-1
        peso=int(input("ingrese el peso del camion "))
        while(peso<=lcamion.tara(ids)):
            print("el peso ingresado es menor a la tara del camion por favor ingrese el peso nuevamente")
            peso=int(input(""))
        total=peso-int(lcamion.tara(ids))
        self.__lista[ids][dia]=int(total)
    def mostrar(self):
        print(self.__lista)
    def mostrarK(self,ids):
        ids=ids-1
        total=0
        for i in range(45):
            total=total+int(self.__lista[ids][i])
        return total
    def listado(self,lcamion,day):
        day=day-1
        print("PATENTE      CONDUCTOR     CANT.KILOS")
        for i in range (20):
            print(lcamion.patente(i).ljust(2," "),lcamion.conductor(i).center(20," "),self.__lista[i][day])
        return

            

        

