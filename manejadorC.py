import csv
from camiones import camion
class Manejadorcamion:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def CargarLista(self):
        archivo = open('camiones.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            camionOBJ=camion(int(fila[0]),fila[1],fila[2],fila[3],float(fila[4]))
            self.__lista.append(camionOBJ)
    def mostrar(self):
        for i in range(len(self.__lista)-1):
            print(self.__lista[i])
    #def buscar(self,ids):
        #for i in range(len(self.__lista)):
            #if(self.__lista[i].getid()==ids):
    def tara(self,ids):
        return self.__lista[ids].gettara()
    def patente(self,ids):
        return (self.__lista[ids].getpatente())
    def conductor(self,ids):
        return (self.__lista[ids].getnom())
    
